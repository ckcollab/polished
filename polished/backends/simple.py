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
        super(SimpleBackend, self).prepare()

    def cleanup(self):
        '''
        Cleanup after prepare() before the next retrieve, make sure you call super!
        '''
        super(SimpleBackend, self).cleanup()
