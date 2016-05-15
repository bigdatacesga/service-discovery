#!/usr/bin/env python

from setuptools import setup

setup(
    name='consul-service-discovery',
    version='0.1.2',
    author='Javier Cacheiro',
    author_email='javier.cacheiro@gmail.com',
    url='https://github.com/javicacheiro/consul-service-discovery',
    license='MIT',
    description='Python client for Consul Service Discovery API',
    long_description=open('README.rst').read(),
    py_modules=['consul'],
    install_requires=['requests'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
