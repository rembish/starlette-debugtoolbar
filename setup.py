#! /usr/bin/env python3
from os.path import join, dirname, abspath
from setuptools import setup, find_packages

here = abspath(dirname(__file__))
requirements = open(join(here, "requirements.txt"))

setup(
    name="Starlette-DebugToolbar",
    version="0.0.0",
    license="BSD",
    author="Aleksey Rembish",
    author_email="alex@rembish.org",
    description="A toolbar overlay for debugging Starlette applications.",
    zip_safe=False,
    platforms="any",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements.readlines()
)
