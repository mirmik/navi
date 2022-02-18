#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import glob
import sys
import os

directory = os.path.dirname(os.path.realpath(__file__))


setup(
    name="navi",
    packages=["navi"],
    version="0.0.1",
    license="MIT",
    description="",
    author="mirmik",
    author_email="mirmikns@yandex.ru",
    url="https://github.com/mirmik/navi",
    long_description=open(os.path.join(
        directory, "README.md"), "r", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    keywords=["testing", "cad"],
    classifiers=[],
    package_data={
        "navi": []
    },
    include_package_data=True,
    install_requires=[],
    extras_require={},
    entry_points={"console_scripts": [
        "navi=navi.__main__:main"
    ]},
)
