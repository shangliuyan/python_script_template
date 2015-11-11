#coding=utf8

import os
import importlib

ENVIRONMENT_VARIABLE = "SETTINGS_MODULE"
empty = object()

class Settings_wrapped(object):
    pass

class Settings(object):

    def __init__(self):
        self._setup()

    def _setup(self):
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        mod = importlib.import_module(settings_module)
        self._wrapped = Settings_wrapped()
        for setting in dir(mod):
            setting_value = getattr(mod, setting)
            setattr(self._wrapped, setting, setting_value)

    def __getattr__(self, name):
        if self._wrapped is empty:
            self._setup()
        return getattr(self._wrapped, name)


settings = Settings()
