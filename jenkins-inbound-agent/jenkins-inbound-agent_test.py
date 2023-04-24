import pytest


@pytest.mark.parametrize("container", ["jenkins-inbound-agent"], indirect=["container"])
def test_certificates_are_present_in_container(container):
    assert container.status == "created"
    # print all CA authorities in ca-certificates:
    authorities = container.run("cat /tmp/ca.txt").output.decode("utf-8")

    assert "CN = Root-CA" in authorities
    assert "DC = local, DC = rki, CN = SUB04-CA" in authorities
