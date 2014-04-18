import subprocess

from base import BaseBackend
from .helpers.timeout import TimeoutError



class SimpleBackend(BaseBackend):
    '''
    The simple backend assumes the repo is already prepared, i.e. static html

    An example of a framework that would use this method might be Django, to `python manage.py migrate`
    and such.
    '''
    URL = 'index.html'

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
