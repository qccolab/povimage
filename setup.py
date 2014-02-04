import os
from setuptools import setup

setup(
        name = "povimage",
        version = "0.0.1",
        author = "Mark Riedesel",
        author_email = "mark@klowner.com",
        packages = ['povimage'],
        scripts = ['scripts/povimage-convert'],
        description = ("Converts a regular image into polar coordinates used "
                "by persistence of vision displays"),
        license = "BSD",

)
