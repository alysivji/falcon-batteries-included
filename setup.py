from setuptools import setup, find_packages

setup(
    name="falcon-batteries-included",
    version="0.0.1",
    description="This example project will demonstrate on how use Falcon and various python libraries to build a REST API for a movie recommendation website.",
    url="https://github.com/alysivji/falcon-batteries-included",
    author="Aly Sivji",
    author_email="alysivji@gmail.com",
    classifiers=["Programming Language :: Python :: 3.6"],
    packages=find_packages(exclude=["scripts", "tests"]),
    install_requires=[""],
    download_url="https://github.com/alysivji/falcon-batteries-included",
)
