import pytest


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee(container):
    assert container.status == "created"


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee_contains_bash(container):
    assert container.exec_run("bash --version").exit_code == 0
