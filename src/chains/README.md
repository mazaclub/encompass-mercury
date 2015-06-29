# Chains

This directory contains definitions of chains. A chain is a class called `Currency` that
inherits the `CryptoCur` class in `cryptocur.py`.

## Chain data

Data about the chain are implemented as class attributes of the Currency class.

Attributes that may be defined:

- `p2pkh_version`: Pay-To-Public-Key-Hash version byte.
- `p2sh_version`: Pay-To-Script-Hash version byte.
- `genesis_hash`: Hex-encoded hash of the genesis block header.
- `coin_name`: Name of the currency.
- `code`: Abbreviation of the currency.
- `irc_nick_prefix`: Prefix that servers prepend to their nicks on IRC.
- `irc_channel`: IRC channel on freenode where servers meet.

## Chainhooks

In addition to the data above, chainhooks provide a way for the chain to 'hook into' the
rest of the program. For example, chainhooks can be used to change the transaction
serialization/deserialization format, as is done in `peercoin.py`.
