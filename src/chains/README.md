# Encompass-Mercury Coin Configuration Files

Encompass supports arbitrary blockchains via .conf files.
The .conf files in this directory can serve as examples
for those wishing to write a .conf file for an arbitrary coin.


## Format

Coin .conf files are in the same format that encompass-mercury.conf is in:
section headers in brackets followed by key: value pairs.

### coin

The `[coin]` section contains chain-specific variables.

- `pubkey_address`: Base58 version byte for Pay-To-Public-Key-Hash addresses.
- `script_address`: Base58 version byte for Pay-To-Script-Hash addresses.
- `genesis_hash`: Hash of the genesis block. Big-endian string of hex digits.
- `code`: Abbreviation for the chain's name. Used in database directory structure.

### hash

The `[hash]` section contains info on which hashing algorithms to use.

- `hash_algo`: General hash algorithm. All other hash options default to this if unspecified.
- `pow_hash`: Hash to use for Proof-of-Work purposes.
- `header_hash`: Hash to use when hashing block headers.
- `base58_hash`: Hash to use in Base58Check encoding.

### coind

The `[coind]` section contains info for communicating with a full node.

- `coind_user`: RPC user. Overrides the `bitcoind_user` in encompass-mercury.conf.
- `coind_password`: RPC password. Overrides the `bitcoind_pass` in encompass-mercury.conf.
- `coind_host`: RPC host. Overrides the `bitcoind_host` in encompass-mercury.conf.
- `coind_port`: RPC port. Override the `bitcoind_port` in encompass-mercury.conf.

### irc

The `[irc]` sections contains info about the IRC channel this chain's servers gather at.

- `irc_channel`: Channel on freenode where server meet to find peers.
  Omit the leading "#" (e.g. "electrum", not "#electrum").
- `server_nick_prefix`: Prefix that servers use in their nicks to identify each other.


## Hashes

These are the valid values for options in the `[hash]` section:

- `sha256`: SHA-256d (Two rounds of SHA-256). The most popular and widely-used algorithm in cryptocurrency.
- `scrypt`: Scrypt Litecoin implementation (N = 1024; r = 1; p = 1).

