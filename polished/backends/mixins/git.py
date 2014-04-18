import subprocess

from polished.backends.helpers.timeout import TimeoutError


class GitMixin(object):

    def get_revision_list(self):
        sha_list_string = subprocess.check_output(['git', 'rev-list', 'master'])
        # be sure to strip leading \n!
        shas = sha_list_string.strip().split('\n')

        for sha in reversed(shas):
            yield sha

    def get_process_revision(self, sha):
        subprocess.call(['git', 'checkout', sha])

        try:
            self.prepare()
            self.screenshot(self.URL)
            self.cleanup()
        except TimeoutError:
            pass
