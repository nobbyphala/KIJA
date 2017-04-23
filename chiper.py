#Nama: I Gede Putu Nobby Aswi Phala
#NRP: 5114100048

import math
import binascii
import sys
from base64 import b64encode,b64decode

P='myuisdfdf'
K='acdtyenu'
K0=bin(int(binascii.hexlify(K[:4]),16))
K1=bin(int(binascii.hexlify(K[4:8]),16))


def encrypt(p):
	Pb=bin(int(binascii.hexlify(p),16))
	ec = int(Pb,2) ^ int(K0,2)
	ec = ec + int(K1,2)
	ec = ec % pow(2,32)
	return binascii.unhexlify('%x' % ec)

def decrypt(c):
	dc=bin(int(binascii.hexlify(c),16))
	dc = int(dc,2)
	dc-=int(K1,2)
	dc%=pow(2,32)
	dc=dc ^ int(K0,2)
	return binascii.unhexlify('%x' % dc)

def multiencrypt(p):
	counter=0
	hasil=''
	while counter<len(p):
		hasil+=encrypt(p[counter:counter+4])
		counter+=4

	return b64encode(hasil) #agar bisa dibaca

def multidecrypt(c):
	p = b64decode(c)
	counter=0
	hasil=''
	while counter<len(p):
		hasil+=decrypt(p[counter:counter+4])
		counter+=4
	
	return hasil

pilihan = raw_input("Pilih encrypt(1) atau decrypt(2): ")
if pilihan == '1':
	plain = raw_input("Masukan text: ")
	print multiencrypt(plain)
elif pilihan == '2':
	chiper = raw_input("Masukan chiper text: ")
	print multidecrypt(chiper)
else:
	print "Argumen tidak dikenal"



