#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
nome = str(input('Qual o seu nome? ')).strip()
input(f'A pessoa tem Silva no nome? {'silva'.upper() in nome.upper()}') #poderia ter usado lower()
