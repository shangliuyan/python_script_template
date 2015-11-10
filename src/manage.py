#coding=utf8

import os
import sys
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--settings", help="define the settings file")
    parser.add_argument(
        "--pythonpath", help="add python path to sys path.")
    args = parser.parse_args()

    if args.pythonpath:
        sys.path.insert(0, options.pythonpath)

    if not args.settings:
        parser.error('--settings arg is requirement')

    os.environ['SETTINGS_MODULE'] = args.settings


if __name__ == "__main__":
    main()
