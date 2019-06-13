import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_atd_service(host):
    """The atd service must be enabled and running
    """
    atd_svc = host.service('atd')

    assert atd_svc.is_running
    assert atd_svc.is_enabled


def test_profile_file(host):
    """The system profile must exist and contain definitions of
    significant variables
    """
    profile_file = host.file('/etc/profile.d/cylc-profile.sh')

    assert profile_file.exists
    assert profile_file.is_file
    assert profile_file.mode == 0o644
    assert profile_file.contains('export CYLC_HOME_ROOT')
    assert profile_file.contains('export CYLC_HOME')
    assert profile_file.contains('export CYLC_VERSION')


def test_cylc_command_exists(host):
    """Must be able to run 'cylc'
    """
    assert host.exists('cylc')


def test_no_zip_files(host):
    """There should be no zip files left in the expected installation directory
    """
    cmd = host.run('ls /opt/*.zip')

    assert cmd.rc != 0
