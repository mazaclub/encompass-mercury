import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 25
    p2sh_version = 85
    genesis_hash = '000001faef25dec4fbcf906e6242621df2c183bf232f263d0ba5b101911e4563'

    coin_name = 'Blackcoin'
    code = 'BLK'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)
