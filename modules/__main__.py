import argparse
import logging
import yaml
from filebackup import FileBackup
from nearlineSync import NearlineSync


def load_config(config_file):
    """Loads a yaml formatted configuration file.

    Keyword arguments:
    config_file -- path to the configuration file
    """
    print "Loading the configuration file"
    with open(config_file, "r") as config:
        return yaml.load(config)


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Runs backup jobs")
    parser.add_argument("config_file", nargs='?',
                        help="path to the config file")
    args = parser.parse_args()
    return args


def main():
    """Entry point"""
    args = parse_args()
    config = load_config(args.config_file)
    # print yaml.dump(config)
    if "file_backup" in config:
        fb = FileBackup(config["file_backup"])
        fb.run()
    if "nearline" in config and config["nearline"]["sync"]:
        ns = NearlineSync(config["nearline"])
        ns.sync()

if __name__ == "__main__":
    sys.exit(main())
