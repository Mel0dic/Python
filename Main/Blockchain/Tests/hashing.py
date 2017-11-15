import hashlib

list1 = ["a", "b", "c"]

def hash_block(self):
	sha = hashlib.sha256()
	sha.update(self)
	return sha.hexdigest()

hash_block("Hash this")