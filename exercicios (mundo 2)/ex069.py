#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
#usuário quer ou não continuar. No final mostre: A) Quantas pessoas tem mais de 18 anos. 
#B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.
cont_h = 0
cont_p = 0
cont_m = 0
while True:
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu gênero [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        print('Opção invalida!')
        sexo = str(input('Qual seu gênero [M/F]: ')).upper().strip()
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20:
        cont_m += 1
    if idade > 18:
        cont_p += 1
    continuar = str(input('Você quer continuar [S/N]? ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        print('Opção invalida!')
        continuar = str(input('Você quer continuar [S/N]? ')).upper().strip()
    if continuar == 'N':
        break
print(f'{cont_p} pessoas tem mais de 18 anos!')
print(f'Foram cadastrados {cont_h} homens!')
print(f'{cont_m} mulheres tem menos de 20 anos!')