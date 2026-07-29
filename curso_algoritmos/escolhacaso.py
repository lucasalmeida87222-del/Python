pacote = "frágil"

match pacote: #O Python segura o pacote na mão e diz: "Deixa eu olhar o que está escrito aqui dentro."
    case "urgente": #Ele pergunta: "O texto é exatamente 'urgente'?" Se não for, ele ignora o que está ali dentro e passa para a linha de baixo.
        print("Enviar de avião imediatamente! ✈️")
        
    case "frágil": #Ele pergunta: "É 'frágil'?" Como a resposta é sim, ele executa a ação de embalar com plástico bolha.
        print("Embalar com plástico bolha e enviar de caminhão. 🚚")
        
    case "comum":
        print("Enviar por transporte padrão. 📦")
        
    case _:
        print("Tipo de pacote desconhecido. Reter para inspeção! 🔍")
#O pulo do gato: Assim que ele encontra o caso certo e executa a instrução, ele ignora todos os outros casos restantes e vai direto para o fim do código. Ele não perde tempo testando o resto!

# O "Default" (case _): O símbolo de underline (_) é o segurança do local. Se chegar um pacote escrito "abacaxi", 
# o Python vai testar todos os casos anteriores, não vai achar nenhum e vai dizer: "Bom, não sei o que é isso, 
# então entrega para o case _ resolver".

#----------------------------------------------------------------------------------------------------------------
# O match...case do Python não serve apenas para comparar textos ou números simples. Ele consegue olhar dentro de 
# estruturas mais complexas, como listas e dicionários.
#Imagine que o seu programa recebe uma lista com o comando e o nome do usuário:
comando = ["entrar", "Lucas"]

match comando:
    # Se a lista tiver a palavra "sair", não importa quem seja
    case ["sair"]:
        print("Até logo!")
        
    # Se a lista tiver a palavra "entrar" seguida de QUALQUER nome,
    # ele já cria a variável 'nome' automaticamente na hora!
    case ["entrar", nome]:
        print(f"Bem-vindo de volta, {nome}! 🎉")
        
    case _:
        print("Comando não reconhecido.")

