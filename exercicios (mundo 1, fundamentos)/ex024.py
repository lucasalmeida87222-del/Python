#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
cidade = str(input('Digite o nome de uma cidade: ')).strip() #tira espaço começo e fim.
input(cidade[0:5].upper()== 'SANTO' ) #usei o upper() para que não tenha problema com letra minuscula.
