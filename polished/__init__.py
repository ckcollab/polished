from .backends.simple import SimpleBackend
from .backends.pelican import PelicanBackend


BACKEND = PelicanBackend()


def take_screenshots():
    sha_list = BACKEND.get_revision_list()
    BACKEND.get_screenshots(sha_list)
