from web3 import Web3;

ganache_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_URL))

account_1 = '0x4433D053B10EbD3a5be8264c14012805E0673828'
account_2 = '0x1BFDEF0C277Fd14C852bF156C128F4d8a4414C53'

private_key = '94617e04214007ecce5b6fec9de39ee4a793d63b9da7e38266b9b4190a5e8241'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(20,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50','gwei')
}


signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
