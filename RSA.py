import math
from cryptography.fernet import Fernet

def RSA(a,h):
    temp = 0
    while(1):
        temp=a%h
        if(temp==0):
            return h
        a=h
        h=temp

p=int(input("Enter your first prime number p: "))
q=int(input("Enter your second prime number q: "))

n=p*q
e=2
phi=(p-1)*(q-1)

while(e<phi):
    if(RSA(e,phi)==1):
        break
    else:
        e+=1

k=2
d=(1+(k*phi))/e

print(d)

msg=12.0

print("Message data = ",msg)

a=input("Enter you msg")

key=Fernet.generate_key()

fernet=Fernet(key)

encMessaage=fernet.encrypt(a.encode())

print("original string : ",a)
print("Encrypted String : ", encMessaage)

decMessage = fernet.decrypt(encMessaage).decode()

print("decrypted string : ",decMessage)
