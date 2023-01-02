def KSA (key):
    key_lenght = len(key)
    S = list (range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key [i % key_lenght]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, n):
    i = 0
    j = 0
    key=[]
    while n>0:
        n=n-1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key

key = 'saputra1'
plaintext = '20060'

def preparing_key_array(s) :
    return[ord(c) for c in s]

key = preparing_key_array(key)

import numpy as np
S = KSA (key)

keystream = np.array ([ord(i) for i in plaintext])
ciper = keystream ^ plaintext 

print (ciper.astype (np.uint8).data.hex())
print ([chr(c) for c in ciper])
