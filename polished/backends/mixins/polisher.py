import inspect
import subprocess

from polished.decorators import polish


class PolisherMixin(object):
    '''
    Searches through the backend for @polish marked functions to call before the HTML is screen captured
    '''
    EXTRA_POLISH_FUNCTIONS = []

    def __init__(self):
        for name, method in inspect.getmembers(self):
            if callable(method) and (hasattr(method, 'polish_urls') or hasattr(method, 'polish_commit_indexes')):
                self.EXTRA_POLISH_FUNCTIONS.append(method)

    def prepare(self):
        self.do_extra_polishing()

    def cleanup(self):
        subprocess.call(["git", "checkout", "."])

    def do_extra_polishing(self):
        '''
        Goes over each EXTRA_POLISH_FUNCTION to see if it applies to this page, if so, calls it
        '''
        for f in self.EXTRA_POLISH_FUNCTIONS:
            if hasattr(f, 'polish_urls') and self.URL in f.polish_urls:
                f()

    @polish(urls=["tree trunk.html"])
    def test_func(self):
        print 'riddeeee'

    @polish(commit_indexes=range(1, 5))
    def test_funcer(self):
        print 'riddeeee'
