# Note : pip install pyDES 
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = b'98487586'
data = b'sinhgad academy'
padded_data = pad(data, DES.block_size)

cipher = DES.new(key, DES.MODE_ECB)

encrypted_data = cipher.encrypt(padded_data)

decrypted_data = cipher.decrypt(encrypted_data)

unpadded_data = unpad(decrypted_data, DES.block_size)

print("Original Data:", data)
print("Padded Data:", padded_data)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
print("Unpadded Data:",unpadded_data)
