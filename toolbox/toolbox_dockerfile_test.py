import pytest


@pytest.mark.parametrize("container", ["toolbox"], indirect=["container"])
def test_aws_cli_is_present_in_container(container):
    assert container.status == "created"
    assert container.run("aws --version").exit_code == 0


@pytest.mark.parametrize("container", ["toolbox"], indirect=["container"])
def test_mtr_is_present_in_container(container):
    assert container.status == "created"
    assert container.run("mtr --version").exit_code == 0
