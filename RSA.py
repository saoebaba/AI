import math
from cryptography.fernet import Fernet

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)


p=int(input("Enter your first prime number p: "))
q=int(input("Enter your second prime number q: "))

n=p*q

e=2
k=2

phi=(p-1)*(q-1)

while(e<phi):
    if(GCD(e,phi)==1):
        break
    else:
        e+=1


d=(1+(k*phi))/e

print(f"Public Key (e,n) : ({e},{n})")
print(f"Private Key (d,n) : ({int(d)},{n})")

a=input("Enter you msg : ")


key=Fernet.generate_key()

fernet=Fernet(key)

encMessaage=fernet.encrypt(a.encode())

print("original string : ",a)
print("Encrypted String : ", encMessaage)

decMessage = fernet.decrypt(encMessaage).decode()

print("decrypted string : ",decMessage)
