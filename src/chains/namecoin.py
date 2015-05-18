import cryptocur
from cryptocur import chainhook
import hashes
from hashes import hash_algos

class Currency(cryptocur.CryptoCur):

    code = 'NMC'
    p2pkh_version = 52
    p2sh_version = 13

    genesis_hash = '000000000062b72c5e2ceb45fbc8587e807c155b0da735e6483dfba2f0a9c770'

    from deserialize import opcodes, script_GetOp, match_decoded
    from utils import hash_160_to_pubkey_address
    @chainhook
    def transaction_get_address_from_output_script(self, bytes, res):
        decoded = [ x for x in script_GetOp(bytes) ]

        # name firstupdate
        match = [ opcodes.OP_2, opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4, opcodes.OP_2DROP,
                opcodes.OP_2DROP, opcodes.OP_DUP, opcodes.OP_HASH160, opcodes.OP_PUSHDATA4, opcodes.OP_EQUALVERIFY, opcodes.OP_CHECKSIG ]
        if match_decoded(decoded, match):
            addr = hash_160_to_pubkey_address(decoded[8][1])
            res['address'] = addr
            return

        # name update
        match = [ opcodes.OP_3, opcodes.OP_PUSHDATA4, opcodes.OP_PUSHDATA4, opcodes.OP_2DROP, opcodes.OP_DROP,
                opcodes.OP_DUP, opcodes.OP_HASH160, opcodes.OP_PUSHDATA4, opcodes.OP_EQUALVERIFY, opcodes.OP_CHECKSIG ]
        if match_decoded(decoded, match):
            addr = hash_160_to_pubkey_address(decoded[7][1])
            res['address'] = addr
            return

    @chainhook
    def blockchain_process_request(blockchain_processor, request, cache_only, res):
        method = request['method']
        params = request.get('params', [])
        result = None

        if method == 'blockchain.name.show':
            res['known_method'] = True
            identifier = str(params[0])
            result = blockchain_processor.bitcoind('name_show', [identifier])

        res['result'] = result
