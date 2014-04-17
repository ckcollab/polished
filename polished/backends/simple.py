import subprocess

from .helpers.screenshot import get_screen_shot
from .helpers.timeout import TimeoutError



class SimpleBackend(object):
    '''
    The simple backend assumes the repo is already prepared, i.e. static html

    An example of a framework that would use this method might be Django, to `python manage.py migrate`
    and such.
    '''
    URL = 'index.html'
    SCREENSHOT_COUNT = 0

    def prepare(self):
        pass

    def take_screenshot(self, url):
        screenshot = get_screen_shot(
            url=url,
            filename="%05d.polished.png" % self.SCREENSHOT_COUNT,
            path="polished/"
        )

        self.SCREENSHOT_COUNT = self.SCREENSHOT_COUNT + 1

    def cleanup(self):
        '''
        Cleanup after prepare() before the next retrieve
        '''
        pass

    def get_revision_list(self):
        sha_list_string = subprocess.check_output(['git', 'rev-list', 'master'])
        # be sure to strip leading \n!
        shas = sha_list_string.strip().split('\n')

        for sha in reversed(shas):
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
        subprocess.call(['git', 'checkout', sha])

        try:
            self.prepare()
            self.take_screenshot(self.URL)
            self.cleanup()
        except TimeoutError:
            pass

    def convert_to_video(self):
        subprocess.call([
            "ffmpeg",
            "-framerate", "3",
            "-pattern_type", "glob",
            "-i", "polished/*.png",
            "polished/output.mp4"
        ])

    def execute(self, url=None):
        if url != None:
            self.URL = url

        for sha in self.get_revision_list():
            self.get_screenshot(sha)

        self.convert_to_video()
