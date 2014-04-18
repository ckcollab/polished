from .helpers.timeout import TimeoutError
from .mixins import GitMixin, PolisherMixin, ScreenshotMixin, VideoMixin


class BaseBackend(GitMixin, PolisherMixin, VideoMixin, ScreenshotMixin):

    URL = 'index.html'
    CURRENT_SHA = None
    CURRENT_COMMIT_INDEX = 0

    def execute(self, url=None):
        if url != None:
            self.URL = url

        for sha in self.get_revision_list():
            self.CURRENT_SHA = sha
            self.CURRENT_COMMIT_INDEX = self.CURRENT_COMMIT_INDEX + 1

            self.checkout(sha)

            try:
                self.prepare()
                self.screenshot(self.URL)
                self.cleanup()
            except TimeoutError:
                pass

        self.convert_to_video()

        self.checkout("master")
