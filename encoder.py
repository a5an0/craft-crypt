#!/usr/bin/env python

class KeyLengthError (Exception):
	def __str__(self):
		return "ERROR: Key shorter than text!"

def encrypt(plaintext, key):
	if len(key) < len(plaintext):
	#	key = (key*2)[:len(plaintext)]
		raise KeyLengthError
	result = ''
	for i in range(len(plaintext)):
		result += chr((((ord(plaintext[i])-32) + (ord(key[i])-32)) % 95) + 32)
	return result

def decrypt(ciphertext, key):
	if len(key) < len(ciphertext):
		raise KeyLengthError
	result = ''
	for i in range(len(ciphertext)):
		result += chr((((ord(ciphertext[i])-32) - (ord(key[i])-32)) % 95) + 32)
	return result
