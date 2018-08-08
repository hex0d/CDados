#######
#######         LEIA!!! - o professor pediu pra usar ASCII - ext, mas é muito trampo desnecessário, então tá usando unicode
#######


import binascii

# Definir a MSG
msg = u"Dados Conversam çç è?"
msg_lengh = len(msg)

def lista_em_binário(msg):
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

lista_em_binário(msg)





