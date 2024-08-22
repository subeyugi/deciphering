#不｢｣ / [全てあなたの所為です。]　解読
#https://youtu.be/MSgpt4kzpNs

import numpy as np # type: ignore
from numpy.linalg import det, inv, eig # type: ignore

n = 8
def toMatrix(s):
    result = [[0] * n for _ in range(n)]
    for i in range(8):
        sep = s[i].split()
        for j in range(n):
            result[i][j] = int(sep[j], 2)
    return np.array(result)

def decodeColor(code):
    hexData = ""
    for i in range(n):
        hexData += "82" + hex(int(code[i], 2))[2:]
    print(hexData)
    return int(hexData, 16).to_bytes(16, byteorder="big").decode("shift-jis", errors="replace")

KenbanCode1 = [
    "1011 0111 0100 0001 1001 0111 0000 0100", \
    "0110 0010 0101 0010 0100 0001 0001 0010", \
    "1100 0111 1000 0000 0111 0110 0010 0000", \
    "0101 0010 0100 0000 0100 0011 0000 0000", \
    "0111 0010 0110 0000 0100 0011 0010 0000", \
    "0111 0100 0011 0000 0111 0101 0000 0000", \
    "0101 0010 0100 0000 0100 0011 0000 0000", \
    "0111 0010 0110 0000 0100 0011 0010 0000"
]

kenbanCode2 = [
    "0111 0010 0101 0000 0100 0010 0011 0000", \
    "1010 0011 1001 0001 1000 0101 0001 0100", \
    "1011 0001 1010 0000 1000 0100 0011 0101", \
    "1000 0011 0110 0011 0111 0101 0001 0110", \
    "1000 0010 0110 0000 0101 0011 0011 0001", \
    "1101 1000 1001 0011 1010 0101 0001 0011", \
    "1000 0010 0110 0000 0101 0000 0011 0011", \
    "1001 0001 1000 0000 0110 0100 0011 0011", \
]

kenbanCode3 = [
    "1111 0110 1010 0110 0110 1010 0000 1001", \
    "1011 0100 1000 0010 0100 0110 0010 0110", \
    "1001 0101 0100 0100 0011 0101 0000 0110", \
    "1001 0100 0110 0011 0100 0101 0000 0111", \
    "0101 0010 0011 0010 0011 0010 0001 0100", \
    "1001 0100 0110 0000 0100 0101 0011 0100", \
    "0111 0100 0100 0000 0100 0100 0010 0100", \
    "0101 0011 0010 0000 0011 0011 0010 0011", \
]


colorCode1 = [
    "10111001", \
    "10101100", \
    "11000101", \
    "11001101", \
    "11001000", \
    "10100010", \
    "11100000", \
    "11001100"
]

colorCode2 = [
    "11111000", \
    "10100010", \
    "11011101", \
    "11100000", \
    "11001000", \
    "10101101", \
    "10101001", \
    "10101100", \
]

colorCode3 = [
    "10101001", \
    "11001101", \
    "10111101", \
    "11000100", \
    "11101001", \
    "10110001", \
    "10100100", \
    "10100010", \
]

A = toMatrix(KenbanCode1)
B = toMatrix(kenbanCode2)
C = toMatrix(kenbanCode3)
invB = np.round(inv(B) * 12).astype(int)

print(invB)
""" D = A * inv(B) * 16
E = np.round(D).astype(int) % 16
for i in range(n):
    s = ""
    for j in range(n):
        if j % 2 == 0: s += "82"
        s += str(hex(E[i][j]))[2:]
    print(s)
 """

print(f"Color1 : {decodeColor(colorCode1)}") #せぎではないもの
print(f"Color2 : {decodeColor(colorCode2)}") #��いみもなくかぎ
print(f"Color3 : {decodeColor(colorCode3)}") #かはたてるこうい

#key : f8a2
