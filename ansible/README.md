# Ansible Server Setup

## Prerequisites

- `ansible` installed locally
- `centos/8` server (change ip in hosts if it changes)

Install docker-compose module:

## Setup Server

```
ansible-playbook -i ./inventories/prod dvzo.yml [--check]
```
