# autotest conftest


def pytest_runtest_setup(item):
    """Kill any lingering deepin-editor before each test.

    Framework session_stop now pkills by app name, but a stale instance
    from outside the test suite (manual launch, ll-cli, etc.) can still
    trigger DBus single-instance and cause the test's session_start to
    redirect to it. This hook ensures a clean slate.
    """
    import subprocess
    subprocess.run("pkill -9 -x deepin-editor", shell=True, check=False)
