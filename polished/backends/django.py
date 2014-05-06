import time
import subprocess

from simple import SimpleBackend


class DjangoBackend(SimpleBackend):
    URL = "http://localhost:8000/"
    PROCESS = None

    def prepare_page(self, *args, **kwargs):
        subprocess.call(["python", "manage.py", "syncdb", "--migrate", "--noinput"])

        if self.PROCESS is not None:
            self.PROCESS.terminate()

        self.PROCESS = subprocess.Popen(["python", "manage.py", "runserver"])

        time.sleep(4)
        super(DjangoBackend, self).prepare_page(*args, **kwargs)

    def cleanup(self):
        self.PROCESS.terminate()

        super(DjangoBackend, self).cleanup()
