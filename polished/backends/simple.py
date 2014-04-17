import subprocess

from polished.screenshot import get_screen_shot



class SimpleBackend(object):
    '''
    The simple backend assumes the repo is already prepared, i.e. static html

    An example of a framework that would use this method might be Django, to `python manage.py migrate`
    and such.
    '''
    URL = 'http://localhost:8000/'

    def prepare(self):
        pass

    def take_screenshot(url, self):
        screenshot = subprocess.call(["webkit2png", url, "-F", "-o", "polished"])

    def cleanup(self):
        '''
        Cleanup after prepare() before the next retrieve
        '''
        pass

    def get_revision_list(self):
        sha_list_string = subprocess.check_output(['git', 'rev-list', 'master'])
        # be sure to strip leading \n!
        shas = sha_list_string.strip().split('\n')

        for sha in shas:
            yield sha


    #def get_screenshots(self, sha_list, start=''):
    #    '''
    #    Start is the optional sha to start images from, otherwise all sha's will be checked out and imagified
    #    '''
    #    sha_not_found = True
    #
    #    for sha in sha_list:
    #        # When we find the right sha, stop skipping and start taking screenshots
    #        if start != '' and sha_not_found:
    #            if sha == start:
    #                sha_not_found = False
    #            else:
    #                continue
    #
    #        self.get_screenshot(sha)


    def get_screenshot(self, sha):
        checkout = subprocess.call('git', 'checkout', sha)

        self.prepare()
        self.take_screenshot(self.URL)
        self.cleanup()

    def execute(self):
        for sha in self.get_revision_list():
            self.get_screenshot(sha)
