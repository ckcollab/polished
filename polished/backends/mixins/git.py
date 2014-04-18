import subprocess

from base import Base


class GitMixin(Base):

    def get_revision_list(self):
        sha_list_string = subprocess.check_output(['git', 'rev-list', 'master'])
        # be sure to strip leading \n!
        shas = sha_list_string.strip().split('\n')

        for sha in reversed(shas):
            yield sha

    def checkout(self, sha):
        subprocess.call(['git', 'checkout', sha])
