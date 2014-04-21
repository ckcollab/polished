import inspect
import subprocess

from base import Base
from polished.decorators import polish


class PolisherMixin(Base):
    '''
    Searches through the backend for @polish marked functions to call before the HTML is screen captured
    '''
    EXTRA_POLISH_FUNCTIONS = []

    def __init__(self, *args, **kwargs):
        for name, method in inspect.getmembers(self):
            if callable(method) and (hasattr(method, 'polish_urls') or hasattr(method, 'polish_commit_indexes')):
                self.EXTRA_POLISH_FUNCTIONS.append(method)

        super(PolisherMixin, self).__init__(*args, **kwargs)

    def prepare_page(self, *args, **kwargs):
        self.do_extra_polishing()
        super(PolisherMixin, self).prepare_page(*args, **kwargs)

    def cleanup(self, *args, **kwargs):
        subprocess.call(["git", "checkout", "."])

        super(PolisherMixin, self).cleanup(*args, **kwargs)

    def do_extra_polishing(self):
        '''
        Goes over each EXTRA_POLISH_FUNCTION to see if it applies to this page, if so, calls it
        '''
        for f in self.EXTRA_POLISH_FUNCTIONS:
            if not hasattr(f, 'polish_commit_indexes'):
                if hasattr(f, 'polish_urls') and self.URL in f.polish_urls:
                    f()

            if not hasattr(f, 'polish_urls'):
                if hasattr(f, 'polish_commit_indexes') and self.CURRENT_COMMIT_INDEX in f.polish_commit_indexes:
                    f()

            if hasattr(f, 'polish_commit_indexes') and hasattr(f, 'polish_urls'):
                if self.URL in f.polish_urls and self.CURRENT_COMMIT_INDEX in f.polish_commit_indexes:
                    f()

