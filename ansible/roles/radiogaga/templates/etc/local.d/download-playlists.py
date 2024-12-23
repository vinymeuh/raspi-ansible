import platform
import tomllib
import urllib.request

hostname = platform.node()
toml_url = f"https://raw.githubusercontent.com/vinymeuh/radiogaga-playlists/refs/heads/main/{hostname}.toml"
local_file = "/tmp/playlists.toml"
output_dir = "/var/lib/mpd/playlists"

try:
    urllib.request.urlretrieve(toml_url, local_file)
except Exception as e:
    print(f"ERROR: unable to download {toml_url} -> {local_file}")
    print(e)
    exit(1)

with open(local_file, "rb") as f:
    data = tomllib.load(f)

if 'playlist' not in data:
    print("ERROR: missing 'playlist' entry in TOML file")
    exit(1)

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
