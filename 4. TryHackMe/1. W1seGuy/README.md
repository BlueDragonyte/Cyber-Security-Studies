\# W1seGuy (TryHackMe)



\## Overview



This room is the first challenge room I've completed. This focused on XOR operation and recovering keys using the operation.





\## Key Concept



XOR relationship:



ciphertext = plaintext ^ key



key = ciphertext ^ plaintext



plaintext = ciphertext ^ key



Note: In Python ^ is the XOR Operator





\##Steps Taken

1. Run NetCat on target IP And Port

!\[Image 1](./images/XOR-1.png)





\## Python Script



To automate XOR operations I created a small script to get the key value



\### xor\_solver.py





