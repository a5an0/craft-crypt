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
    

