import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 137
    p2sh_version = 5
    genesis_hash = '00000c3ce6b3d823a35224a39798eca9ad889966aeb5a9da7b960ffb9869db35'

    coin_name = 'Clam'
    code = 'CLAMS'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)

        clamspeech_size = ('clamspeech_size', vds.read_compact_size, False)
        clamspeech = ('clamspeech', 'read_bytes:clamspeech_size', True)
        fields.append(clamspeech_size)
        fields.append(clamspeech)
