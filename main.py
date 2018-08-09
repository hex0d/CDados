#######
#######         LEIA!!! - o professor pediu pra usar ASCII - ext, mas é muito trampo desnecessário, então tá usando unicode/utf-8
#######                 CONVERSOR = https://onlinebinarytools.com/convert-binary-to-utf8







def main():
    msg = input("Mensagem?: ")
    opt = input("Modo Jumento ou não Jumento? (1 ou 2) ")
    opt = int(opt)
    if opt == 1:
        bin_msg(msg)
    elif opt == 2:
        bin_msg_python(msg)
    else:
        print('Opção errada')
        main()
        return 0




## função para transformar a string em binário do modo fácil
def bin_msg_python(msg):
    answ = ''.join(format(ord(i),'b').zfill(8) for i in msg)
    print(answ)


## função para transformar a string em binário do modo difícil
def bin_msg(msg):
    ###### listas para transformar em binário

    #coloca

    msg_list = list(msg)

    #mensagem em binário porem vem no formato

    msg_bin = []

    #mensagem faltando

    msg_nofill= []

    #LISTA da mensagem completa
    msg_complete = []


    for i in msg_list:
        msg_bin.append(bin(ord(i)))

    for i in msg_bin:
        msg_nofill.append(i[2:])

    for i in msg_nofill:
        msg_complete.append(i.zfill(8))

    msg_complete_str = ''.join(msg_complete)



    print(msg_complete_str)



main()





