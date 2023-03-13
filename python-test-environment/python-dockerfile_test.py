import pytest
import subprocess


@pytest.mark.parametrize("container", ["python-test-environment"], indirect=["container"])
def test_jupyter(container):
    assert container.status == "created"
    assert container.run("poetry --version").exit_code == 0


@pytest.mark.parametrize("container", ["python-test-environment"], indirect=["container"])
def test_jupyter_git(container):
    assert container.status == "created"
    assert container.run("make --version").exit_code == 0


@pytest.mark.parametrize("container", ["python-test-environment"], indirect=["container"])
def test_container_has_poetry(container):
    assert container.status == "created"
    assert container.run("poetry --version").exit_code == 0


@pytest.mark.parametrize("container", ["python-test-environment"], indirect=["container"])
def test_can_use_poetry_in_container(container, tmp_path):
    d = tmp_path / "pyproject.toml"
    d.parent.rmdir()
    d.parent.mkdir()
    d.touch()
    d.write_text(PYPROJECT_CONTENT)
    # create valid pyproject.toml in container
    assert container.status == "created"
    subprocess.run(["docker", "cp", str(d), f"{container.id}:/home/testuser/pyproject.toml"])
    print(container.run("ls -la").output)
    assert container.run("poetry install").exit_code == 0


PYPROJECT_CONTENT = """
[tool.poetry]
name = "jovyan"
version = "0.1.0"
description = ""
authors = ["jakob"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
ramda = "^0.7.6"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""
