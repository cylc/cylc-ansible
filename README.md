# The cylc-core Ansible Role
[Ansible] Role for the installation of the [Cylc] workflow engine.

The **cylc-coer** role installs cylc (into the `/opt` directory) and adjusts
the system-wide `PATH` environment variable so all users have access to it
by placing a file in `/etc/profile.d`.

## Role variables
Available variables and default values (see defaults/main.yml): -

    cylc_version: 7.8.2

## Example playbook

    ---
    - hosts: cylc-server
      tasks:
      - include_role:
          name: alanbchristie.cylc-core

---

[Ansible]: https://pypi.org/project/ansible/
[Cylc]: https://cylc.github.io
