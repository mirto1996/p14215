﻿from bitarray import bitarray
import mmh3
 
class BloomFilter:
text=raw_input()    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "Nope"
        return "Probably"
 
bf = BloomFilter(500000, 7)
 
lines = open("/usr/share/dict/american-english").read().splitlines()
for line in lines:
    bf.add(line)
if bit_array[b1] == 1 and bit_array[b2] == 1:
    print "Probably in set"
else:
    print "---bit_array---"
