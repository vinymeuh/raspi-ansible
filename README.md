# raspi-ansible

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A set of [Ansible](https://www.ansible.com/) playbooks to setup and to manage [Alpine Linux](https://alpinelinux.org/) on my little fleet of Raspberry Pi.

## Install Ansible

Assuming Python 3 interpreter is already installed:

```
~> python -m venv venv
~> source venv/bin/activate
~> pip install -r requirements.txt  
```

## Bootstrapping Apline Linux installation

```
~> source venv/bin/activate
~> ansible-playbook bootstrap.yml -e target=pizerow
```