# Standard Modules
import os
import re

# Django Modules
from django.conf import settings
from django.shortcuts import render

# Project Modules
from .helpers import cut


def index(request):
    template = "viewer/index.html"
    context = {}

    try:
        images = os.listdir(
            os.path.join(
                settings.BASE_DIR, "viewer", "static", "viewer", "images"
            )
        )
    except FileNotFoundError:
        images = []

    context["images"] = sorted(images, key=cut)

    return render(request, template, context)
