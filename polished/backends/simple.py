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
