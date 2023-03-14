import pytest


@pytest.mark.parametrize("container", ["smee-proxy"], indirect=["container"])
def test_smee(container):
    assert container.status == "created"
