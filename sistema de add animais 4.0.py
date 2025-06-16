import sys
import json
import os

base_dir = os.path.dirname(__file__)
animais_file = os.path.join(base_dir, 'animais.json')
adotantes_file = os.path.join(base_dir, 'adotantes.json')
ongs_file = os.path.join(base_dir, 'ongs.json')

def carregar_dados(caminho):
    try:
        with open(caminho, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

animais = carregar_dados(animais_file)
adotantes = carregar_dados(adotantes_file)
ongs = carregar_dados(ongs_file)


while True:
    print("\n=== Plataforma de Adoção de Animais ===")
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

    escolha = input("Escolha uma opção: ").strip()

    if escolha == '1':
        especie = input("Espécie: ").strip()
        raca = input("Raça: ").strip()
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit():
                break
            print("Digite uma idade válida (somente números).")
        personalidade = input("Personalidade: ").strip()
        historico_medico = input("Histórico Médico: ").strip()

        animal = {
            "especie": especie,
            "raca": raca,
            "idade": idade,
            "personalidade": personalidade,
            "historico_medico": historico_medico,
        }

        animais.append(animal)
        with open(animais_file, "w") as f:
            json.dump(animais, f, indent=4)
        print("Animal cadastrado com sucesso!")

    elif escolha == '2':
        nome = input("Nome: ").strip()
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit():
                break
            print("Digite uma idade válida (somente números).")
        preferencias = input("Preferências (separe por vírgulas): ").split(",")
        estilo_vida = input("Estilo de vida: ").strip()

        adotante = {
            "nome": nome,
            "idade": idade,
            "preferencias": [p.strip() for p in preferencias],
            "estilo_vida": estilo_vida
        }

        adotantes.append(adotante)
        with open(adotantes_file, 'w') as f:
            json.dump(adotantes, f, indent=4)
        print("Adotante cadastrado com sucesso!")

    elif escolha == '3':
        nome = input("Nome da ONG: ").strip()
        localizacao = input("Localização: ").strip()
        contato = input("Contato: ").strip()
        missao = input("Missão: ").strip()

        ong = {
            "nome": nome,
            "localizacao": localizacao,
            "contato": contato,
            "missao": missao
        }

        ongs.append(ong)
        with open(ongs_file, 'w') as f:
            json.dump(ongs, f, indent=4)
        print("ONG cadastrada com sucesso!")

    elif escolha == '4':
        print("\nONGs cadastradas:")
        if not ongs:
            print("Nenhuma ONG cadastrada.")
        for ong in ongs:
            print(f"- {ong['nome']} | Local: {ong['localizacao']} | Contato: {ong['contato']} | Missão: {ong['missao']}")

    elif escolha == '5':
        print("\nAnimais cadastrados:")
        if not animais:
            print("Nenhum animal cadastrado.")
        for i, animal in enumerate(animais, start=1):
            print(f"{i}. {animal['especie']} {animal['raca']} ({animal['idade']} anos) - {animal['personalidade']}")
            print(f"   Histórico médico: {animal['historico_medico']}")

    elif escolha == '6':
        print("\nAdotantes cadastrados:")
        if not adotantes:
            print("Nenhum adotante cadastrado.")
        for i, adotante in enumerate(adotantes, start=1):
            preferencias = ', '.join(adotante['preferencias'])
            print(f"{i}. {adotante['nome']} ({adotante['idade']} anos) - Preferências: {preferencias} | Estilo de vida: {adotante['estilo_vida']}")

    elif escolha == '7':
        print("\nAnimais cadastrados:")
        for i, animal in enumerate(animais):
            print(f"{i + 1}. {animal['especie']} {animal['raca']}")
        try:
            index = int(input("Digite o número do animal que deseja excluir: ")) - 1
            if 0 <= index < len(animais):
                animais.pop(index)
                with open(animais_file, 'w') as f:
                    json.dump(animais, f, indent=4)
                print("Animal excluído com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    elif escolha == '8':
        print("\nAdotantes cadastrados:")
        for i, adotante in enumerate(adotantes):
            print(f"{i + 1}. {adotante['nome']}")
        try:
            index = int(input("Digite o número do adotante que deseja excluir: ")) - 1
            if 0 <= index < len(adotantes):
                adotantes.pop(index)
                with open(adotantes_file, 'w') as f:
                    json.dump(adotantes, f, indent=4)
                print("Adotante excluído com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    elif escolha == '9':
        print("\nONGs cadastradas:")
        for i, ong in enumerate(ongs):
            print(f"{i + 1}. {ong['nome']}")
        try:
            index = int(input("Digite o número da ONG que deseja excluir: ")) - 1
            if 0 <= index < len(ongs):
                ongs.pop(index)
                with open(ongs_file, 'w') as f:
                    json.dump(ongs, f, indent=4)
                print("ONG excluída com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    elif escolha == '10':
        print("Saindo do sistema. Até mais!")
        sys.exit()

    else:
        print("Opção inválida. Tente novamente.")