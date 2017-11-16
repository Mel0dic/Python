import hashlib

class Block:
	def __init__(self, previouseHash, transactions):
		self.previouseHash = previouseHash
		self.transactions = transactions
		self.blockHash = self.hashBlock()

	def hashBlock(self):
		sha = hashlib.sha256()
		sha.update(str(self.transactions).encode('utf-8') +
					str(self.previouseHash).encode('utf-8'))
		return sha.hexdigest()











genesisTransaction = ["satoshi sent 10 bitcoin", "someone sent 10 bitcoin"]

myBlock = Block("0", genesisTransaction)

print(myBlock.blockHash)

block2Transactions = ["everyone lost their bitcoin", "bitcoin"]

myBlock2 = Block(myBlock.blockHash, block2Transactions)

print(myBlock2.blockHash)