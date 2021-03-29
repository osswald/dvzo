# Ansible Server Setup

## Prerequisites

- `ansible` installed locally
- `centos/8` server (change ip in hosts if it changes)

Install docker-compose module:

## Setup Server

```
ansible-vault decrypt ./inventories/prod/group_vars/all.yml
ansible-playbook -i ./inventories/prod dvzo.yml [--check]
ansible-vault encrypt ./inventories/prod/group_vars/all.yml
```
