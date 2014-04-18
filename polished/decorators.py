from functools import wraps



def polish(commit_indexes=None, urls=None):
    '''
    Apply certain behaviors to commits or URLs that need polishing before they are ready for screenshots

    For example, if you have 10 commits in a row where static file links were broken, you could re-write the html
    in memory as it is interpreted.

    Keyword arguments:
    commit_indexes -- A list of indexes to apply the wrapped function to
    url -- A list of URLs to apply the wrapped function to
    '''
    def decorator(f):
        if commit_indexes:
            f.polish_commit_indexes = commit_indexes
        if urls:
            f.polish_urls = urls

        @wraps(f)
        def wrappee(*args, **kwargs):
            return f(*args, **kwargs)

        return wrappee

    return decorator
