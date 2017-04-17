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

def satukanargumen(): # untuk inputan bersepasi
	if(len(sys.argv)>3):
		hasil=''
		for i in range(2, len(sys.argv)):
			hasil+=sys.argv[i]
			if (i != len(sys.argv)-1):
				hasil+= ' '

		return hasil
	else:
		return sys.argv[2]


#meriksa argument

if(sys.argv[1]=='--encrypt'):
	print multiencrypt(satukanargumen())
elif (sys.argv[1]=='--decrypt'):
	print multidecrypt(sys.argv[2])
else:
	print "Argument tidak dikenal"



