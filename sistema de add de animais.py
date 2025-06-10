import sys
import json

animais = []
adotantes = []
ongs = []

# logim 
while True:
    print("=== Plataforma de Adocao de Animais ===")
    print("1. Adicionar Animal")
    print("2. Cadastrar Adotante")
    print("3. Cadastrar ONG")
    print("4. Listar ONGs")
    print("5. Listar Animais")
    print("6. Listar Adotantes")
    print("7. Excluir Animal")
    print("8. Excluir Adotante")
    print("9. Excluir ONG")
    print("10. Sair")

    escolha = input("Escolha uma opcao: ").strip()
    
    # Adicionar animais 
    if escolha == '1':
        especie = input("Especie: ").strip()
        raca = input("Raca: ").strip()
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit():
                break
            print("Digite uma idade válida (somente números).")
        personalidade = input("Personalidade: ").strip()
        historico_medico = input("Historico Medico: ").strip()

        animal = {
            "especie": especie,
            "raca": raca,
            "idade": idade,
            "personalidade": personalidade,
            "historico_medico": historico_medico,
        }
        
        try:
            with open("C:/Users/Romão/Downloads/trabalho de aeda/animais.json", "r") as f:
                animais_listados = json.load(f)
        except:
            print("erro, não conseguiu abrir o arquivo")
            animais_listados = []  # <- se der erro, garante que a lista não esteja indefinida

    # animal já deve ter sido criado antes desse bloco
        animais_listados.append(animal)

        try:
            with open("C:/Users/Romão/Downloads/trabalho de aeda/animais.json", "w") as f:
                json.dump(animais_listados, f, indent=4)
        except:
            print("erro ao salvar a lista")

        print("Animal cadastrado com sucesso!")


    # Cadastro de adotantes 
    elif escolha == '2':
        nome = input("Nome: ").strip()
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit():
                break
            print("Digite uma idade válida (somente números).")# Não verifica se é número
        preferencias = input("Preferencias (separe por virgulas): ").split(",")
        estilo_vida = input("Estilo de vida: ").strip()

        adotante = {
            "nome": nome,
            "idade": idade,
            "preferencias": preferencias,
            "estilo_vida": estilo_vida
        }
        adotantes.append(adotante)
        print("Adotante cadastrado com sucesso!")

    # Cadastro de ONGs
    elif escolha == '3':
        nome = input("Nome da ONG: ").strip()
        localizacao = input("Localizacao: ").strip()
        contato = input("Contato: ").strip()
        missao = input("Missao: ").strip()

        ong = {
            "nome": nome,
            "localizacao": localizacao,
            "contato": contato,
            "missao": missao
        }
        ongs.append(ong)
        print("ONG cadastrada com sucesso!")

    # ONGs cadastradas 
    elif escolha == '4':
        print("ONGs cadastradas:")
        for ong in ongs:
            print("- " + ong['nome'] + " | Local: " + ong['localizacao'] + " | Contato: " + ong['contato'] + " | Missao: " + ong['missao'])

    # Todos os animais cadastrados 
    elif escolha == '5':
        try:
            with open("C:/Users/Romão/Downloads/trabalho de aeda/animais.json", "r") as f:
                animais = json.load(f)
        except:
            print("erro, não conseguiu abrir o arquivo")

        print("Animais cadastrados:")
        contador = 1
        for animal in animais:
            print(str(contador) + ". " + animal['especie'] + " " + animal['raca'] + " (" + animal['idade'] + " anos) - " + animal['personalidade'])
            print("   Historico medico: " + animal['historico_medico'])
            contador += 1

    # Lista dos adotantes
    elif escolha == '6':
        print("Adotantes cadastrados:")
        contador = 1
        for adotante in adotantes:
            preferencias = ', '.join(adotante['preferencias'])
            print(str(contador) + ". " + adotante['nome'] + " (" + adotante['idade'] + " anos) - Preferencias: " + preferencias + " | Estilo de vida: " + adotante['estilo_vida'])
            contador += 1

    # Excluir Animal
    elif escolha == '7':
        print("Animais cadastrados:")
        for i, animal in enumerate(animais):
            print(f"{i + 1}. {animal['especie']} {animal['raca']}")
        index = int(input("Digite o número do animal que deseja excluir: ")) - 1
        if 0 <= index < len(animais):
            animais.pop(index)
            print("Animal excluído com sucesso!")
        else:
            print("Número inválido.")

    # Excluir Adotante
    elif escolha == '8':
        print("Adotantes cadastrados:")
        for i, adotante in enumerate(adotantes):
            print(f"{i + 1}. {adotante['nome']}")
        index = int(input("Digite o número do adotante que deseja excluir: ")) - 1
        if 0 <= index < len(adotantes):
            adotantes.pop(index)
            print("Adotante excluído com sucesso!")
        else:
            print("Número inválido.")

    # Excluir ONG
    elif escolha == '9':
        print("ONGs cadastradas:")
        for i, ong in enumerate(ongs):
            print(f"{i + 1}. {ong['nome']}")
        index = int(input("Digite o número da ONG que deseja excluir: ")) - 1
        if 0 <= index < len(ongs):
            ongs.pop(index)
            print("ONG excluída com sucesso!")
        else:
            print("Número inválido.")

    # Sair do sistema 
    elif escolha == '10':
        print("Saindo do sistema. Ate mais!")
        sys.exit()

    # Opção inválida 
    else:
        print("Opcao invalida. Tente novamente.")
