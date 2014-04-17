import subprocess

from simple import SimpleBackend


class PelicanBackend(SimpleBackend):
    URL = 'output/index.html'

    def prepare(self):
        subprocess.call(["make", "html"])
