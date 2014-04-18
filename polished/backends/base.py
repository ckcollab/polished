import subprocess

from .helpers.timeout import TimeoutError
from .mixins import GitMixin, PolisherMixin, DriverMixin, VideoMixin


class BaseBackend(GitMixin, PolisherMixin, VideoMixin, DriverMixin):

    URL = 'index.html'
    CURRENT_SHA = None
    CURRENT_COMMIT_INDEX = 0

    def __init__(self, *args, **kwargs):
        subprocess.call(["rm", "-rf", "polished_output/*.png"])

        super(BaseBackend, self).__init__(*args, **kwargs)

    def execute(self, url=None):
        if url != None:
            self.URL = url

        for sha in self.get_revision_list():
            self.CURRENT_SHA = sha
            self.CURRENT_COMMIT_INDEX = self.CURRENT_COMMIT_INDEX + 1

            self.checkout(sha)

            try:
                self.prepare()
                self.go_to_url(url)
                self.prepare_page()
                self.screenshot()
                self.cleanup()
            except TimeoutError:
                pass

        self.convert_to_video()

        self.dispose()

    def dispose(self, *args, **kwargs):
        self.checkout("master")
        super(BaseBackend, self).dispose(*args, **kwargs)
