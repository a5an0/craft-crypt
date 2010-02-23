#!/usr/bin/env python

def encrypt(plaintext, key):
	if len(key) < len(plaintext):
		key = (key*2)[:len(plaintext)]
	result = ''
	for i in range(len(plaintext)):
		result += chr((((ord(plaintext[i])-32) + (ord(key[i])-32)) % 95) + 32)
	return result

def decrypt(ciphertext, key):
	result = ''
	for i in range(len(ciphertext)):
		result += chr((((ord(ciphertext[i])-32) - (ord(key[i])-32)) % 95) + 32)
	return result
