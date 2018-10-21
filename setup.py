import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyint",
    version="1.0.0",
    author="Projjol Banerji",
    author_email="ping@projjol.me",
    description="Python implementation of protobuf style varints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Projjol/pyint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)