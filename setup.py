from setuptools import setup

setup(
    name="encompass-mercury",
    version="0.1",
    scripts=['run_encompass_mercury','encompass-mercury'],
    install_requires=[
        'plyvel',
        'jsonrpclib',
        'irc>=11',
        # scrypt 1024 (i.e. litecoin scrypt)
        'ltc_scrypt==1.0'
    ],
    package_dir={
        'encompassmercury':'src'
        },
    py_modules=[
        'encompassmercury.__init__',
        'encompassmercury.utils',
        'encompassmercury.storage',
        'encompassmercury.storage_base',
        'encompassmercury.storage_leveldb',
        'encompassmercury.deserialize',
        'encompassmercury.blockchain_processor',
        'encompassmercury.server_processor',
        'encompassmercury.processor',
        'encompassmercury.version',
        'encompassmercury.ircthread',
        'encompassmercury.stratum_tcp',
        'encompassmercury.stratum_http',
        'encompassmercury.chainparams',
        'encompassmercury.chains.__init__',
        'encompassmercury.chains.hashes',
        'encompassmercury.chains.cryptocur',
        'encompassmercury.chains.bitcoin',
        'encompassmercury.chains.mazacoin'
    ],
    description="Encompass Mercury Server",
    author="Tyler Willis",
    author_email="kefkius@mail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/mazaclub/encompass-mercury",
    long_description="""Multi-coin server for the Encompass multi-coin wallet"""
)


