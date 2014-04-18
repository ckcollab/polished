import fnmatch
import glob
import os

from .helpers.timeout import TimeoutError
from .mixins import GitMixin, PolisherMixin, DriverMixin, VideoMixin


class BaseBackend(GitMixin, PolisherMixin, VideoMixin, DriverMixin):

    URL = 'index.html'
    CURRENT_SHA = None
    CURRENT_COMMIT_INDEX = 0

    def __init__(self, *args, **kwargs):
        self._remove_files("polished_output", "*.png")

        super(BaseBackend, self).__init__(*args, **kwargs)

    def execute(self, url=None):
        if url != None:
            self.URL = url
        else:
            url = self.URL

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

    def _remove_files(self, directory, pattern):
        '''
        Removes all files matching the search path

        Arguments:
        search_path -- The path you would like to remove, can contain wildcards

        Example:
        self._remove_files("output/*.html")
        '''
        for root, dirnames, file_names in os.walk(directory):
            for file_name in fnmatch.filter(file_names, pattern):
                os.remove(os.path.join(root, file_name))
