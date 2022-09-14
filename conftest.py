import os

import docker
import pytest


class TrackedContainer:
    def __init__(self, dockerfile_path, image_name):
        self.client = docker.from_env()
        self.image = self.client.images.build(path=dockerfile_path, tag=image_name)[0]
        self.container = self.client.containers.run(self.image, detach=True, tty=True)
        print(self.container.logs())

    def run(self, command, **kwargs):
        return self.container.exec_run(command, **kwargs)

    @property
    def api(self):
        return self.client.api

    @property
    def id(self):
        return self.container.id

    @property
    def status(self):
        return self.container.status

    def __del__(self):
        self.container.remove(force=True)


@pytest.fixture(scope="function")
def container(request) -> TrackedContainer:
    dockerfile_path = os.path.join(os.path.dirname(__file__), request.param)
    print(dockerfile_path)
    container = TrackedContainer(dockerfile_path, request.param)
    yield container
    del container
