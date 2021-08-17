#!/usr/bin/env python3

from setuptools import setup
from subprocess import check_output

version = check_output(["git", "describe", "--tags", "--always"])[:-1].decode()


setup(
	name="tango-w1therm",
	version=version,
	description="Tango Device Server for digital temperature sensors using w1_therm driver",
	author="Grzegorz Kowalski (daneos)",
	author_email="daneos@daneos.com",
	url="https://github.com/daneos/tango-w1therm",
	license="GPLv3",
	scripts=["w1therm"],
	packages=["tango_w1therm"],
	package_dir={"tango_w1therm": "."}
)
