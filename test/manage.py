#coding=utf8

import os
import sys
import argparse
import importlib

#from test.test_settings import test_settings 

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
        return

    os.environ['SETTINGS_MODULE'] = args.settings
    mod = importlib.import_module("test.test_settings")
    
    mod.test_settings()

    


if __name__ == "__main__":
    os.environ.setdefault("SETTINGS_MODULE", "configs")
    main()
