i=0
msg = '0111010101100010'
msg_len=len(msg)
list_bin = []
list_MTL = []

for digit in msg:
    list_bin.append(int(digit))

def num_MLT(num):
    i=num%4
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i == 2:
        return 0
    if i == 3:
        return -1


for x in list_bin:
    if x == 0:
        list_MTL.append(num_MLT(i))
    if x == 1:
        i += 1
        list_MTL.append(num_MLT(i))


print(list_MTL)