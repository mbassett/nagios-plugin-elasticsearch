#!/usr/bin/env python

from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

setup(
    name="nagios-plugin-elasticsearch",
    description="An ElasticSearch availability and performance monitoring plugin for Nagios.",
    version="1.2.0",
    packages=find_packages(),
    url="https://github.com/anchor/nagios-plugin-elasticsearch",
    maintainer="Sharif Olorin",
    maintainer_email="sio@tesser.org",
    author="Saj Goonatilleke",
    author_email="sg@redu.cx",
    scripts=["check_elasticsearch"],
    license="MIT",
    install_requires=[
      'nagioscheck==0.1.6',
      'simplejson>=3.4.0',
      'setuptools>=3.4.0',
      'pip>=1.4'
    ],
    include_package_data=True
)
