# The cylc_core Ansible Role

[![Build Status](https://travis-ci.org/alanbchristie/cylc_core.svg?branch=master)](https://travis-ci.org/alanbchristie/cylc_core)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

An [Ansible] Role for the installation of the [Cylc] v7.x workflow engine.

The **cylc_core** role installs cylc (into the `/opt` directory).
The term _core_ is used here as this Role is a minimal installation
suitable for a _headless_ server, i.e. one without graphical/display
capabilities. **cylc_core** is a Role for a Cylc engine that's expected to
be configured and used from the command-line.

## Role variables
Available variables and default values
(see [defaults/main.yml](defaults/main.yml)): -

    # The Cylc version to install, where: -
    # 7.0.0 <= cylc_version < 8.0.0
    cylc_version: 7.8.3

## Example playbook

    ---
    - hosts: cylc-server
      tasks:
      - include_role:
          name: alanbchristie.cylc_core

---

[Ansible]: https://pypi.org/project/ansible/
[Cylc]: https://cylc.github.io
