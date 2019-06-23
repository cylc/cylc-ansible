# The Cylc Ansible Role

[![Build Status](https://travis-ci.org/alanbchristie/cylc.svg?branch=master)](https://travis-ci.org/alanbchristie/cylc)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

An [Ansible] Role for the installation of the [Cylc] v7.x workflow engine.

Cylc is a workflow engine for cycling systems originally developed for
operational environmental forecasting at NIWA by Dr Hilary Oliver.
It is now an Open Source collaboration involving NIWA, Met Office, and others.
It is available under the GPL v3 license.

## Role variables
Available variables and default values
(see [defaults/main.yml](defaults/main.yml)): -

    # The Cylc version to install, where: -
    # 7.0.0 <= cylc_version < 8.0.0
    cylc_version: 7.8.3

    # Whether to install the optional GUI components
    # like PyGTK, graphviz etc. Setting this variable
    # only makes sense for a host that has a DISPLAY.
    cylc_visualisation: no

## Example playbook

    ---
    - hosts: cylc
      tasks:
      - include_role:
          name: alanbchristie.cylc
        vars:
          cylc_version: 7.8.2
          cylc_visualisation: yes

---

[Ansible]: https://pypi.org/project/ansible/
[Cylc]: https://cylc.github.io
