
def to_bin(msg): # Returns the array of each bit and the binary message
    array_msg = []
    char_bin= [format(ord(c), 'b').zfill(8) for c in msg]
    bin_msg = ''.join(char_bin)
    for c in bin_msg:
        array_msg.append(int(c))
    return {'bin_msg':bin_msg, #binary message
            'array_msg':array_msg} # array of bits- [0, 1, 1, 1, 1, 1, 1, 0, 0]

def to_MLT(array_msg): #transform from binary list to MLT-3 array
    i=0
    MLT_check = [0,1,0,-1]
    MLT_array =[]
    for x in array_msg:
        if x == 0:
            MLT_array.append(MLT_check[i%4])
        if x == 1:
            i += 1
            MLT_array.append(MLT_check[i%4])
    return MLT_array

def main():
    '''msg = str(input('Mensagem: '))
    bin_msg = to_bin(msg)
    print('Mensagem em Binário: '+ bin_msg['bin_msg'])
    print('Mensagem em MLT-3: '+ ''.join(str(to_MLT(bin_msg['array_msg']))))'''
    a = to_MLT([1,0,1,1,0,1,0])
    print(a,type(a))

    b = ''.join(str(x) for x in a)
    print(b[3])

if __name__ == "__main__":
    main()

