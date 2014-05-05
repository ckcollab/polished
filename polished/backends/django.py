

# call syncdb --migrate --noinput
#
# call_command('syncdb', interactive = False)

class DjangoBackend(object):
    def __init__(self, *args, **kwargs):
        raise NotImplemented("This isn't implemented yet!")
