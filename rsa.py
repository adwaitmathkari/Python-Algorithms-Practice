from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

# print(keyPair)
# print(type(keyPair))
# print(keyPair[0])
# print("______________________XXXXXXXXXXXXXXXXXXXX_--------------------------------")
pubKey = keyPair.publickey()
print(f"Public key:  (n={pubKey.n}, e={pubKey.e})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))



# Encrypt
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print(encrypted)
print("Encrypted:", binascii.hexlify(encrypted))


"""
1. Suppose that you intercepted the message 
[7478675787667008073846555210022, 9675104303065935004013959501807, 7853661332689580386483880056370,9547579452582041595499349328596, 7714456104498337564236407616764] 
being encrypted using RSA with the public key 
n := 14219056659976765469909553590911, e := 8345. 
Using the fact that n is small, read the message which was encoded using the encodings A = 11, B = 12,...,Z= 36. 


"""



# Decrypt

n=14219056659976765469909553590911
e=8345

# key = RSA.construct((n,e))
# decryptor = PKCS1_OAEP.new(key)
# decrypted = decryptor.decrypt("[7478675787667008073846555210022, 9675104303065935004013959501807, 7853661332689580386483880056370, 9547579452582041595499349328596, 7714456104498337564236407616764]")
# print('Decrypted:', decrypted)


print((7478675787667008073846555210022**e)%n)