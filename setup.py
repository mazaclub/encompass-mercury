from setuptools import setup

setup(
    name="encompass-mercury",
    version="0.9",
    scripts=['run_encompass_mercury','encompass-mercury'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'encompassmercury':'src'
        },
    py_modules=[
        'encompassmercury.__init__',
        'encompassmercury.chainparams',
        'encompassmercury.utils',
        'encompassmercury.storage',
        'encompassmercury.deserialize',
        'encompassmercury.networks',
        'encompassmercury.blockchain_processor',
        'encompassmercury.server_processor',
        'encompassmercury.processor',
        'encompassmercury.version',
        'encompassmercury.ircthread',
        'encompassmercury.stratum_tcp',
        'encompassmercury.stratum_http',
        'encompassmercury.chains.__init__',
        'encompassmercury.chains.cryptocur',
        'encompassmercury.chains.mazacoin'
    ],
    description="Multi-Coin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum Lightweight Wallets"""
)


