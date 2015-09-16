import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 30
    p2sh_version = 33
    genesis_hash = '00000fc63692467faeb20cdb3b53200dc601d75bdfa1001463304cc790d77278'

    coin_name = 'DogecoinDark'
    code = 'DOGED'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)
    
    irc_nick_prefix = 'EL_'
    irc_channel = '#electrum-doged'
