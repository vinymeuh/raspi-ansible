# raspi-ansible

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A collection of [Ansible](https://www.ansible.com/) playbooks to setup and manage [Alpine Linux](https://alpinelinux.org/) on my little fleet of Raspberry Pi.

## Bootstrapping Alpine Linux installation

1. **Mount the SD Card** to your system at a specified mount directory (`mntdir`).
2. Run the **bootstrap.yml** playbook to download and extract the Alpine Linux distribution onto the SD Card. This playbook also performs basic setup, enabling remote access to the Raspberry Pi upon the first boot.

```shell
ansible-playbook playbooks/bootstrap.yml -e target=radiogaga -e mntdir=/run/media/viny/RADIOGAGA
```

3. **Eject the SD Card** and insert it into the Raspberry Pi.
4. **Boot the Raspberry Pi**.
5. **Connect remotely** as the pi user via SSH to complete the initial setup of Alpine Linux manually.

```shell
doas su -
apk update
apk add python3
lbu commit -d
```

6. Verify connectivity with Ansible.

```shell
ansible --one-line -m ping pizerow
```

## Additional system configuration

THe first time:

```shell
ansible-galaxy collection install -r requirements.yml
```

Ten to apply further configuration settings, run the dedicated playbook:

```shell
ansible-playbook playbooks/pizerow.yml
```
