[![Build Status](https://travis-ci.org/alanbchristie/cylc-ansible.svg?branch=master)](https://travis-ci.org/alanbchristie/cylc-ansible)

# cylc-ansible
[Ansible] playbook for the installation of the [Cylc] workflow engine.

There is one role: -

-   **cylc**

The **cylc** role installs cylc (into the `/opt` directory) and adjusts the
system-wide `PATH` environment variable so all users have access to it
by placing a file in `/etc/profile.d`. A `cylc` user is added and given
password-less sudo privilege.

## Running the playbook
On your _control machine_ you will need [Python] (ideally a Python 3 virtual
environment) and the project requirements: -

    $ conda activate cylc-ansible
    $ pip install -r requirements.txt

You will also need to provide an Ansible inventory file to define
the `cylcserver` host before installing with something like: -

    $ ansible-playbook site.yml -i <inventory file>

>   `inventory.yml` is safe to use. It is prevented from being committed
    as it's in the project's `.gitigore` file.

---

[Ansible]: https://pypi.org/project/ansible/
[Cylc]: https://cylc.github.io
[Python]: https://www.python.org
