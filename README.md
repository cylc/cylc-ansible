[![Build Status](https://travis-ci.org/alanbchristie/cylc-ansible.svg?branch=master)](https://travis-ci.org/alanbchristie/cylc-ansible)

# cylc-ansible
[Ansible] playbook for the installation of the [Cylc] workflow engine.

There are two roles: -

-   **cylc**
-   **environment**

The `cylc` role installs cylc (into the `/opt` directory) and adjusts the
system-wide `PATH` environment variable so all users have access to it
by placing a file in `/etc/profile.d`. A `cylc` user is added and given
password-less sudo privilege.

The `enviornment` role installs Python 3 (3.6) and creates a virtual
environment for the supplied user which also becomes their default
environment as it adjusts the user's `.baschrc` file.

## Running the roles
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
