# stringHandler.py - Functions to handle encrypting and decrypting strings of text 
#
# Copyright (C) 2010  Alex Schoof
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import blowfish

def encryptString(plaintext, key):
    """ 
    Takes in a string and a key, encrypts with blowfish, and returns the ciphertext string 
    
    TODO: Add different modes of operation (CBC, etc.)
    """
    blowfish.genSubkeys(key)
    # pad the plaintext
    pt = plaintext + ((8 - (len(plaintext) % 8)) * chr(0))
    print pt
    textGroups = []
    while(pt != ""):
        textGroups.append(pt[:8])
        pt = pt[8:]
    
    ciphertext = ""
    # ECB mode
    for t in textGroups:
        l, r = blowfish.strToInt(t[:4]), blowfish.strToInt(t[4:])
        l, r = blowfish.encrypt(l, r)
        l, r = blowfish.intToString(l), blowfish.intToString(r)
        ciphertext += l + r
    return ciphertext
    
def decryptString(ciphertext, key):
    """ 
    Takes in a string and a key, decrypts with blowfish, and returns the plaintext string 
    
    TODO: Add different modes of operation (CBC, etc.)
    """
    blowfish.genSubkeys(key)
    
    ct = ciphertext
    textGroups = []
    while(ct != ""):
        textGroups.append(ct[:8])
        ct = ct[8:]
    
    plaintext = ""
    # ECB mode
    for t in textGroups:
        l, r = blowfish.strToInt(t[:4]), blowfish.strToInt(t[4:])
        l, r = blowfish.encrypt(l, r)
        l, r = blowfish.intToString(l), blowfish.intToString(r)
        plaintext += l + r
    return plaintext
