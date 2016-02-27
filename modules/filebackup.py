import os
import shutil
import subprocess
import time


class FileBackup(object):
    """Manages the backup jobs"""
    def __init__(self, config):
        super(FileBackup, self).__init__()
        self.config = config

    def run(self):
        """Runs the backup job"""
        print "Running the backup jobs"
        for source in self.config["sources"]:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            backup_dir = "{0}/{1}/{2}".format(self.config["backup_destination_dir"],
                                              source["backup_dir"],
                                              timestamp)
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            if "server" in source:
                cmd = "rsync -ah \
                      {0}@{1}:{2} {3}".format(source["remote_user"],
                                              source["server"],
                                              source["directory"],
                                              backup_dir)
            else:
                cmd = "rsync -avh {0} {1}".format(source["directory"],
                                                  backup_dir)
            subprocess.call(cmd, shell=True)
            if self.config["archive"]:
                print "Archiving the backup..."
                archive_path = backup_dir + ".tar.gz"
                cmd = "tar -czf {0} -C {1} .".format(archive_path, backup_dir)
                subprocess.call(cmd, shell=True)
                shutil.rmtree(backup_dir)
