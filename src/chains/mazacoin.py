import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 50
    p2sh_version = 9
    genesis_hash = '00000c7c73d8ce604178dae13f0fc6ec0be3275614366d44b1b4b5c6e238c60c'

    coin_name = 'Mazacoin'
    code = 'MZC'

    irc_channel = '#tate-wallet'
