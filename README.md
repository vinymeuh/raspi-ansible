# raspi-ansible

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A set of [Ansible](https://www.ansible.com/) playbooks to setup and to manage [Alpine Linux](https://alpinelinux.org/) on my little fleet of Raspberry Pi.

## Bootstrapping Alpine Linux installation

Mount the SD Card then use the **bootstrap.yml** playbook. It downloads the Alpine Linux distribution, extracts it on the SD Card and performs minimal setup to be able to connect remotely to the Raspberry Pi just after the first boot.

```shell
ansible-playbook playbooks/bootstrap.yml -e target=pizerow
```

Eject the SD card and use it to boot the Raspberry Pi.

We should be able to connect remotely as root using ssh to manually (:bow:) finish the Alpine setup.

```shell
cd /media/mmcblk0p1
setup-alpine -f setup.answer        # Accept all defaults choices
apk add wpa_supplicant              # If wifi enabled
rc-update add wpa_supplicant boot   # If wifi enabled
rm -f /etc/runlevels/default/bootstrap-*
apk update
apk add python3
lbu commit -d
reboot
```

After reboot we should be able to ping the Raspberry Pi with ```ansible```:

```shell
ansible --one-line -m ping pizerow
```
