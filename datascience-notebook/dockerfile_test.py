import pytest


@pytest.mark.parametrize("container", ["datascience-notebook"], indirect=["container"])
def test_jupyter(container):
    assert container.status == "created"
    assert container.run("jupyter --version").exit_code == 0


@pytest.mark.parametrize("container", ["datascience-notebook"], indirect=['container'])
def test_jupyter_git(container):
    assert container.status == "created"
    assert container.run("git --version").exit_code == 0

