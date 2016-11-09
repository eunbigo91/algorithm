class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0]) * 100 + ord(string[1])
        return value
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 7269
print hash_table.calculate_hash_value('HELLO')

# Test lookup edge case
# Should be -1
print hash_table.lookup('HELLO')

# Test store
hash_table.store('HELLO')
# Should be 7269
print hash_table.lookup('HELLO')

# Test store edge case
hash_table.store('HELLOER')
# Should be 7269
print hash_table.lookup('HELLOER')
