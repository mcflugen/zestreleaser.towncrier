# -*- coding: utf-8 -*-
"""Installer for the zestreleaser.towncrier package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='zestreleaser.towncrier',
    version='1.0a1',
    description="zest.releaser plugin to call towncrier",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='Python Plone',
    author='Maurits van Rees',
    author_email='m.van.rees@zestsoftware.nl',
    url='https://pypi.org/project/zestreleaser.towncrier',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['zestreleaser'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'toml',
        'towncrier',
        'zest.releaser',
    ],
    entry_points={
        'zest.releaser.prereleaser.middle': [
            # Call towncrier to update the changelog with newsfragments:
            'call_towncrier = zestreleaser.towncrier:call_towncrier',
        ],
        'zest.releaser.prereleaser.before': [
            # Check if towncrier is available and configured:
            'check_towncrier = zestreleaser.towncrier:check_towncrier',
        ],
        'zest.releaser.postreleaser.before': [
            # We only need to check if towncrier is available and
            # configured for this project.
            # Then the history should not be changed.
            'check_towncrier = zestreleaser.towncrier:check_towncrier',
        ],
    },
)
