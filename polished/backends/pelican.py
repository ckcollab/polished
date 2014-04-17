import subprocess

from .helpers.timeout import timeout
from simple import SimpleBackend


class PelicanBackend(SimpleBackend):
    URL = 'output/index.html'

    @timeout(30)
    def prepare(self):
        subprocess.call(["make", "html"])
