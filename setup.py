import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyransac",
    version="1.0.0",
    author="Adam Morrissett",
    author_email="me@adamlm.com",
    description="A general random sample consensus (RANSAC) package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MeelonUsk/pyransac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Program Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
