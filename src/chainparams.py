"""Interface for interacting with a chain"""

import chains

blockchains = []
active_chain = None

def init_chains():
#    import imp, __builtin__, os, pkgutil
    import imp, os, pkgutil
    global blockchains

#    if __builtin__.use_local_modules:
#        fp, pathname, description = imp.find_module('chains')
#        chain_names = [name for a, name, b in pkgutil.iter_modules([pathname])]
#        chain_names = filter(lambda name: os.path.exists(os.path.join(pathname,name+'.py')), chain_name)
#        imp.load_module('encompassmercury.chains', fp, pathname, description)
#        chain_modules = map(lambda name: imp.load_source('encompassmercury.chains.'+name, os.path.join(pathname,name+'.py')), chain_names)
#    else:
#        chain_names = [name for a, name, b in pkgutil.iter_modules(chains.__path__)]
#        chain_modules = [ __import__('encompassmercury.chains.'+name, fromlist=['encompassmercury.chains']) for name in chain_names]

    chain_names = [name for a, name, b in pkgutil.iter_modules(chains.__path__)]
    chain_modules = [ __import__('encompassmercury.chains.'+name, fromlist=['encompassmercury.chains']) for name in chain_names]

    # these are not actual currency modules, so skip them
    non_coins = ['cryptocur', 'hashes']
    for name, c in zip(chain_names, chain_modules):
        if name in non_coins:
            continue
        try:
            blockchains.append( c.Currency() )
        except Exception:
            print("Cannot initialize coin {}!".format(name))

def get_active_chain():
    if len(blockchains) == 0:
        init_chains()
    global active_chain
    return active_chain

def set_active_chain(chaincode):
    if len(blockchains) == 0:
        init_chains()
    global active_chain
    active_chain = get_chain_instance(chaincode)

def get_chain_instance(chaincode):
    for c in blockchains:
        if chaincode.upper() == c.code.upper():
            return c
