# NC [IP] [Port] returns the ciphertext. But requires a key as input to get the flag.
# Ciphertext changes each time you listen in.
# The below script deciphers the key by using XOR Operation ^
# Where key = cipher text  XOR known plaintext (From analysing the .py file downloaded source of th lab)
# Known output flag structure is THM{[unknown value]}

ciphertext = "321a293329573308262d232a10092d126607233a273c167b380a1e1d200c14261d782c142a2b3a24"
known_char = b"THM{"
cipher_b = bytes.fromhex(ciphertext)    # converts the ciphertext hex values into bytes
key_bytes = []                          # integer values after XOR of known platext bytes against ciphertext bytes

#Loop through length of plaintext
for index in range (len(known_char)):
    cb = cipher_b[index]                # ciphertext bytes
    kb = known_char[index]              # plaintext bytes
    key_bytes.append(cb ^ kb)           # XOR the cipher bytes and the known character bytes and inserts to key_bytes variable
    
key_fragment = bytes(key_bytes)         # Convert list of integer values to bytes

print (key_fragment)                    # test output value

# Key length is 5 so we know the key repeated k0,k1,k2,3k,k4,k0... 
# We know only the first 4
# K=5 --> This is found in the .py file
# Next step is to bruteforce the last key
# Ciphertext = key ^ plantext
# Plaintext = key ^ ciphertext

#Try all combinations from 0 - 255 for 5th (k4)
for k4 in range(256):
    full_key = key_fragment + bytes([k4])  
    
    plaintext = bytes (
        cipher_b[i] ^ full_key[i % len(full_key)]
        for i in range (len(cipher_b))
    )
    
    try:
        deciphered_text = plaintext.decode()
        if deciphered_text.endswith("}"):
            print(full_key)
            print(deciphered_text)
    except:
        pass