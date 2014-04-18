from .helpers.timeout import TimeoutError
from .mixins import GitMixin, PolisherMixin, DriverMixin, VideoMixin


class BaseBackend(GitMixin, PolisherMixin, VideoMixin, DriverMixin):

    URL = 'index.html'
    CURRENT_SHA = None
    CURRENT_COMMIT_INDEX = 0

    def prepare(self):
        '''
        After changing git revisions, prepare the repository, make sure you call super!
        '''
        super(BaseBackend, self).prepare()

    def prepare_page(self, *args, **kwargs):
        '''
        This is called after the page has been loaded, good time to do extra polishing
        '''
        super(BaseBackend, self).prepare_page(*args, **kwargs)

    def cleanup(self):
        '''
        Cleanup after prepare() before the next retrieve, make sure you call super!
        '''
        super(BaseBackend, self).cleanup()

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
