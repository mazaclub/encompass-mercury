# Encompass-Mercury Coin Configuration Modules

Encompass supports arbitrary blockchains via modules.
The modules files in this directory can serve as examples
for those wishing to write a module for an arbitrary coin.


## Format

The base class `CryptoCur` is largely self-explanatory.
The class for a currency should be named `Currency`, or, it can be named anything such as `CoinClassName`,
but a statement, `Currency = CoinClassName`, must be present after the class definition.

The attributes that need to be defined are as follows:

- `code`: Abbreviation for the currency (e.g. BTC, MZC).
- `p2pkh_version`: Base58 Pay-To-Public-Key-Hash version.
- `p2sh_version`: Base58 Pay-To-Script-Hash version.
- `genesis_hash`: Hash of the genesis block.


### hash algorithms

Info on which hashing algorithms to use.

- `hash_algo`: General hash algorithm. All other hash options default to this if unspecified.
- `pow_hash`: Hash to use for Proof-of-Work purposes.
- `header_hash`: Hash to use when hashing block headers.
- `base58_hash`: Hash to use in Base58Check encoding.

### irc

Info about the IRC channel this chain's servers gather at.

- `irc_channel`: Channel on freenode where server meet to find peers.
- `server_nick_prefix`: Prefix that servers use in their nicks to identify each other.


## Hashes

These are the valid values for the `hash_*` class attributes.
The `hash_algos` dictionary is defined in hashes.py.

- `sha256`: SHA-256d (Two rounds of SHA-256). The most popular and widely-used algorithm in cryptocurrency.
- `scrypt`: Scrypt Litecoin implementation (N = 1024; r = 1; p = 1).

