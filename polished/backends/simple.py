import subprocess

from base import BaseBackend
from .helpers.timeout import TimeoutError



class SimpleBackend(BaseBackend):
    '''
    The simple backend assumes the repo is already prepared, i.e. static HTML

    An example situation might be if you were making a simple static site for your mum's cleaning service, nothing
    needs to be generated/cleaned up, the HTML is already there!
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
