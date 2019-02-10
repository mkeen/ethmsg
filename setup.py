import setuptools
from distutils.command.build_py import build_py as _build_py

with open("README.md", "r") as fh:
    long_description = fh.read()

class inst_solc(_build_py):
    from solc import install_solc
    install_solc('v0.4.25')
    
setuptools.setup(
    name="ethmsg",
    version="0.0.1",
    author="Mike Keen",
    author_email="mkeen.atl@gmail.com",
    description="A simple Ethereum message sender",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkeen/ethmsg",
    packages=setuptools.find_packages(),
    install_requires=['click', 'web3', 'py-solc', 'eth-tester'],
    scripts=['bin/ethmsg'],
    cmdclass={'inst_solc': inst_solc},
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
