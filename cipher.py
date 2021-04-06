import sys
cipher = int(sys.argv[1])
code = sys.stdin.read()
length_code = len(code)
cracked = False
encode = ''
store_val = bool()
import string
while not cracked:
    for k in range(length_code):
        ch = code[k]
        if ch.isupper():
          store_val = True
        elif ch.islower():
          store_val = False
        ch = ch.upper()
        if ch == " " or ch in string.punctuation :
          total = ord(ch)
        else:
          total = ord(ch) + cipher
        if total >90 and ch not in string.punctuation and ch != " ":
          total = total-26
        elif total < 65 and ch not in string.punctuation and ch != " ":
          total = total + 26
        output_code = chr(total)
        if output_code not in string.punctuation:
          result = output_code
        if store_val == True:
          result = result.upper()
        elif store_val == False:
          result = result.lower()
        encode = encode + result
    cracked = True
    k= encode.upper()
g= ''
for j in k:
    if j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        g= g + j
a = 0
for x in range(5,len(g),5):
    print(g[a:x], end =' ')
    a = x

print(g[x:(len(g)+1)])


