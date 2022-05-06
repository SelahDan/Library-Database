#!/usr/bin/env python
# coding: utf-8

# In[3]:


hash_table = [[] for _ in range(10000)]
# hashing function
def hashing_func(key):
    sum=0
   
        
    return sum %len(hash_table)
# using hashing function we can insert values into the table 
def insert(hash_table, key, value):
    hash_key = hashing_func(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))
        
#searching the table for a book when the         
def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v


# In[ ]:




