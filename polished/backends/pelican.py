import subprocess

from .helpers.timeout import timeout
from simple import SimpleBackend


class PelicanBackend(SimpleBackend):
    URL = 'output/index.html'

    def __init__(self, *args, **kwargs):
        self._remove_files("output/*.html")

        super(PelicanBackend, self).__init__(*args, **kwargs)

    @timeout(30)
    def prepare(self):
        subprocess.call(["make", "html"])

        super(PelicanBackend, self).prepare()
