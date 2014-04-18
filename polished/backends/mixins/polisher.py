import inspect

from polished.decorators import polish



class PolisherMixin(object):
    '''
    Searches through the backend for @polish marked functions to call before the HTML is screen captured
    '''
    POLISH_FUNCTIONS = []

    def _get_marked_funcs(self):
        # 'polish_url' in my_func.__dict__
        # 'polish_commit_indexes' in my_func.__dict__

        # inspect.isfunction(method)

        print self.__dict__
        pass

    @polish(url="tree trunk")
    def test_func(self):
        print 'riddeeee'
