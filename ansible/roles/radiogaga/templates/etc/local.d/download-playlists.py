import os
import platform
import time
import tomllib
import urllib.request

hostname = platform.node()
toml_url = f"https://raw.githubusercontent.com/vinymeuh/radiogaga-playlists/refs/heads/main/{hostname}.toml"
local_file = "/tmp/playlists.toml"
output_dir = "/var/lib/mpd/playlists"


def download_playlists():
    try:
        urllib.request.urlretrieve(toml_url, local_file)
    except Exception as e:
        print(f"ERROR: unable to download {toml_url} -> {local_file}")
        print(e)
        return

    with open(local_file, "rb") as f:
        data = tomllib.load(f)

    if 'playlist' not in data:
        print("ERROR: missing 'playlist' entry in TOML file")
        return

    for playlist in data['playlist']:
        try:
            with open(f"{output_dir}/{playlist['name']}.m3u", "w") as f:
                txt = (
                    f"""#EXTM3U\n"""
                    f"""#EXTINF:0,{playlist['name']}\n"""
                    f"""{playlist['url']}\n"""
                )
                f.write(txt)
        except Exception as e:
            print(e)

    if 'start' in data:
        try:
            with open(f"/tmp/playlist.start", "w") as f:
                f.write(data['start'])
        except Exception as e:
            print(e)

if __name__ == "__main__":
    retry = 0
    while True:
        download_playlists()
        if len(os.listdir(output_dir)) > 0 or retry > 11:
            break
        time.sleep(10);
        retry += 1
