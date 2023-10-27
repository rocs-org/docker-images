import pytest


@pytest.mark.parametrize("container", ["node-chrome"], indirect=["container"])
def test_jupyter(container):
    assert container.status == "created"
    assert container.run("node --version").exit_code == 0
