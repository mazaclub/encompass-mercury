# Encompass-Mercury Coin Configuration Modules

Encompass supports arbitrary blockchains via modules.
The modules files in this directory can serve as examples
for those wishing to write a module for an arbitrary coin.


## Format

The base class `CryptoCur` is largely self-explanatory.


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

These are the valid values for the `hash_*` class attributes:

- `sha256`: SHA-256d (Two rounds of SHA-256). The most popular and widely-used algorithm in cryptocurrency.
- `scrypt`: Scrypt Litecoin implementation (N = 1024; r = 1; p = 1).

