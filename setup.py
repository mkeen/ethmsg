import setuptools
from distutils.core import setup
    
setuptools.setup(
    name="ethmsg",
    version="0.0.1",
    author="Mike Keen",
    author_email="mkeen.atl@gmail.com",
    description="A simple Ethereum message sender",
    long_description="A simple Ethereum message sender",
    url="https://github.com/mkeen/ethmsg",
    packages=['ethmsg'],
    install_requires=['click', 'web3', 'py-solc', 'eth-tester', 'eth-account'],
    scripts=['bin/ethmsg', 'bin/ethrd'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
