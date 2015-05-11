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
        'encompassmercury.stratum_http'
    ],
    description="Encompass Mercury Server",
    author="Tyler Willis",
    author_email="kefkius@mail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/mazaclub/encompass-mercury",
    long_description="""Multi-coin server for the Encompass multi-coin wallet"""
)


