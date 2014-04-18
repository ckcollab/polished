import subprocess

from .mixins import GitMixin, ScreenshotMixin, VideoMixin



class SimpleBackend(GitMixin, VideoMixin, ScreenshotMixin):
    '''
    The simple backend assumes the repo is already prepared, i.e. static html

    An example of a framework that would use this method might be Django, to `python manage.py migrate`
    and such.
    '''
    DEFAULT_URL = 'index.html'

    def prepare(self):
        '''
        After changing git revisions, prepare the repository
        '''
        pass

    def cleanup(self):
        '''
        Cleanup after prepare() before the next retrieve
        '''
        pass

    def execute(self, url=None):
        if url != None:
            self.URL = url

        for sha in self.get_revision_list():
            self.get_process_revision(sha)

        self.convert_to_video()
