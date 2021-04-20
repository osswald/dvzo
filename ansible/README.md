# Ansible Server Setup

## Prerequisites

- `ansible` installed locally
- `centos/8` server (change ip in hosts if it changes)

### Ansible Galaxy Packages

```
ansible-galaxy collection install community.general
```

### Setup a user

```
mkdir /home/dvzo
groupadd dvzo
useradd -M -d /home/dvzo -g dvzo -s /bin/bash
chown dvzo:dvzo /home/dvzo -R
usermod -aG wheel dvzo

# set this to no in /etc/ssh/sshd_config
PermitRootLogin no
# set this to no as well
PasswordAuthentication no
# restart sshd
systemctl restart sshd
```

## Setup Server

```
ansible-vault decrypt ./inventories/prod/group_vars/all.yml
ansible-playbook -i ./inventories/prod dvzo.yml [--check] -K
>> dvzo-user-password
ansible-vault encrypt ./inventories/prod/group_vars/all.yml
```
