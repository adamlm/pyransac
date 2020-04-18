"""pyransac package details.

This module contains the package details for pyransac.
"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="pyransac",
    version="1.1.1",
    author="Adam Morrissett",
    author_email="me@adamlm.com",
    description="A general random sample consensus (RANSAC) package",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="random sample consensus ransac",
    url="https://github.com/MeelonUsk/pyransac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
