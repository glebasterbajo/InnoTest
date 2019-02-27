# Standard Modules
import os
import multiprocessing

# Project Modules
from .helpers import create_screenshots

# Django Modules
from django.apps import AppConfig


class ViewerConfig(AppConfig):
    name = "viewer"

    def ready(self):
        process = multiprocessing.Process(target=create_screenshots)
        process.start()
