#######
#######         LEIA!!! - o professor pediu pra usar ASCII - ext,
#######                  mas é muito trampo desnecessário, então tá usando unicode/utf-8
#######                 CONVERSOR = https://onlinebinarytools.com/convert-binary-to-utf8







def main():


    mensagem = input("Mensagem?: ")
    opcao_escolhida = input("Modo Jumento ou não Jumento? (1 ou 2) ")
    opcao_escolhida = int(opcao_escolhida)

    mensagem_binaria = gerar_mensagem_jeito_selecionado(opcao_escolhida, mensagem)
    print('Mensagem em binario: ' + mensagem_binaria)


def gerar_mensagem_jeito_selecionado(opcao_escolhida, mensagem):
    # Fazer do jeito facil
    if opcao_escolhida == 2:
        mensagem_binaria = transformar_string_para_binario_facil(mensagem)

    # Fazer do jeito dificil
    elif opcao_escolhida == 1:
        mensagem_binaria = transformar_string_para_binario_dificil(mensagem)

    else:
        print('Opção errada')
        main()

    return mensagem_binaria



def transformar_string_para_binario_facil(mensagem):
    for caracter in mensagem:
        mensagem_binaria = ''.join(format(ord(caracter),'b').zfill(8))
    return mensagem_binaria



def transformar_string_para_binario_dificil(mensagem):
    caracteres_da_mensagem = list(mensagem)

    # 0b01000001
    mensagem_binario_formatada = transformar_para_binario_formatado(caracteres_da_mensagem)

    #   01000001
    mensagem_binario_puro = transformar_binario_formatado_em_puro(mensagem_binario_formatada)

    string_mensagem_binaria = criar_string_mensagem_binaria(mensagem_binario_puro)
    return string_mensagem_binaria



def transformar_para_binario_formatado(caracteres_da_mensagem):
    mensagem_binario_formatada = []
    for caracter in caracteres_da_mensagem:
        caracter_em_binario = bin(ord(caracter))
        mensagem_binario_formatada.append(caracter_em_binario)

    return mensagem_binario_formatada



def transformar_binario_formatado_em_puro(mensagem_binario_formatada):
    mensagem_binario_puro = []
    for bit in mensagem_binario_formatada:
        mensagem_binario_puro.append(bit[2:])

    return mensagem_binario_puro



def criar_string_mensagem_binaria(mensagem_binario_puro):
    mensagem_binaria = []
    for bit in mensagem_binario_puro:
        mensagem_binaria.append(bit.zfill(8))

    string_mensagem_binaria = ''.join(mensagem_binaria)
    return string_mensagem_binaria


main()
