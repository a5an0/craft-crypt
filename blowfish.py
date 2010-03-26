# blowfish.py - a pure-python implementation of Blowfish
#   as specified here: http://www.schneier.com/paper-blowfish-fse.html
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

ROUNDS = 16 # You shouldn't change this unless you have a good reason
CONSTANTS_FILE = 'blowfish_constants.py'
S, P = []

def encrypt(xL, xR):
    """ 
    Encrypt two plaintext halves xL and xR using the generated subkeys. 
    Returns the encrytped halves 
    """
    # Work through the Feistel network
    for i in range(ROUNDS):
        xL ^= P[i]
        xR = F(xL) ^ xR
        tmp = xL
        xL = xR
        xR = tmp
    # undo last swap
    tmp = xL
    xL = xR
    xR = tmp
    xR ^= P[ROUNDS]
    xL ^= P[ROUNDS+1]
    return xL, xR

def decrypt(xL, xR):
    """ 
    Decrypt two ciphertext halves xL and xR using the generated subkeys. 
    Returns the decrypted halves 
    """
    # Work through the Feistel network
    for i in range(ROUNDS):
        xL ^= P[-(i+1)]
        xR = F(xL) ^ xR
        tmp = xL
        xL = xR
        xR = tmp
    # undo last swap
    tmp = xL
    xL = xR
    xR = tmp
    xR ^= P[1]
    xL ^= P[0]
    return xL, xR

def genSubkeys(key):
    """ Use key to generate all the subkeys needed for encryption/decryption """
    S = sboxes
    # Generate P-Boxes needed for subkey generation
    j = 0
    for i in range(ROUNDS+2):
        data = 0L
        for k in range(4):
            data = (data << 8) | ord(key[j])
            j += 1
            if (j >= len(key)):
                j = 0
        P[i] = parray[i] ^ data
    # Generate subkey P-Boxes
    datal, datar = 0L, 0L
    for i in range(ROUNDS+2):
        datal, datar = encrypt(datal, datar)
        P[i] = datal
        P[i+1] = datar
    # Generate  subkey S-boxes
    for i in range(4):
        for j in range(256):
            datal, datar = encrypt(datal, datar)
            S[i][j] = datal
            S[i][j+1] = datar

def F(x):
    """ F function used in each round """
    d = x & 0x00FF
    x >>= 8
    c = x & 0x00FF
    x >>= 8
    b = x & 0x00FF
    x >>= 8
    a = x & 0x00FF
    f = (S[0][a] + S[1][b] ^ S[2][c]) + S[3][d]
    return f
    

