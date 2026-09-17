#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: # pra saber se a lista pilha esta vazia ou não.
            pilha.pop() # se ela não tiver vazia eu vou excluir o ultimo elemento. obs: Cada vez que ter um parenteses ( eu coloquei o pop para que se tiver outro( ele exclua até aparecer um ).
        else:
            pilha.append(')')
            break
if len (pilha) == 0: # Assim vou saber se a cada ( abrindo teve um ) fechando.
    print('Sua expressão está válida!')
else:
    print('Sua espressão está errada!')