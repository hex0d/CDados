import binascii


msg = "Dados Conversam çç è?"

test2 = []

test = list(msg)

for i in test:
    test2.append(bin(ord(i)))

print(test2)






