import os.path
import subprocess
import shlex


class NearlineSync(object):
    """Manages Goole Nearline stuff"""
    def __init__(self, config):
        super(NearlineSync, self).__init__()
        self.config = config

    def sync(self):
        """Syncs data to Google Nearline"""
        # self._check_gsutil()
        for directory in self.config["sync_dirs"]:
            cmd = "gsutil -m rsync -d -r "
            cmd += "-x '.*\.DS_Store' "
            cmd += "{0} gs://{1}/{2}/{3}".format(directory, self.config["bucket"],
                                                 self.config["directory"],
                                                 os.path.basename(directory))
            subprocess.call(cmd, shell=True)
