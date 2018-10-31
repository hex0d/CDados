msg = '0111010101100010111010101001010'
msg_len=len(msg)
list_bin = []
list_MTL = []
list_MTL2 = []

for digit in msg:
    list_bin.append(int(digit))

def MLT_iter(num):
    i=num%4
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i == 2:
        return 0
    if i == 3:
        return -1

def a(list_bin):
    i=0
    for x in list_bin:
        if x == 0:
            list_MTL.append(MLT_iter(i))
        if x == 1:
            i += 1
            list_MTL.append(MLT_iter(i))

def b(list_bin):
    i=0
    MLT_check = [0,1,0,-1]
    for x in list_bin:
        if x == 0:
            list_MTL.append(MLT_check[i%4])
        if x == 1:
            i += 1
            list_MTL.append(MLT_check[i%4])


if a(list_bin) == b(list_bin):
    print('suave')