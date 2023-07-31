import pytest


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee(container):
    assert container.status == "created"


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee_contains_bash(container):
    assert container.run("bash --version").exit_code == 0


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee_contains_curl(container):
    assert container.run("curl --version").exit_code == 0


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee_contains_node(container):
    assert container.run("node --version").exit_code == 0


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee_container_has_smee_cli(container):
    assert container.status == "created"
    assert container.run("smee --version").exit_code == 0
