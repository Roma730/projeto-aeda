import sys
import json
import os

# Caminho base onde os arquivos JSON serão armazenados
base_dir = os.path.dirname(__file__)
path_animais = os.path.join(base_dir, 'animais.json')
path_adotantes = os.path.join(base_dir, 'adotantes.json')
path_ongs = os.path.join(base_dir, 'ongs.json')

# Funções utilitárias
def carregar_dados(caminho):
    try:
        with open(caminho, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(caminho, dados):
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4)

# Carrega os dados iniciais
animais = carregar_dados(path_animais)
adotantes = carregar_dados(path_adotantes)
ongs = carregar_dados(path_ongs)

# Loop principal
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
                idade = int(idade)
                break
            print("Digite uma idade válida.")
        personalidade = input("Personalidade: ").strip()
        historico_medico = input("Histórico Médico: ").strip()

        animal = {
            "especie": especie,
            "raca": raca,
            "idade": idade,
            "personalidade": personalidade,
            "historico_medico": historico_medico
        }

        animais.append(animal)
        salvar_dados(path_animais, animais)
        print("✅ Animal cadastrado com sucesso!")

    elif escolha == '2':
        nome = input("Nome: ").strip()
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit():
                idade = int(idade)
                break
            print("Digite uma idade válida.")
        preferencias = input("Preferências (separe por vírgulas): ").strip().split(',')
        estilo_vida = input("Estilo de vida: ").strip()

        adotante = {
            "nome": nome,
            "idade": idade,
            "preferencias": [p.strip() for p in preferencias],
            "estilo_vida": estilo_vida
        }

        adotantes.append(adotante)
        salvar_dados(path_adotantes, adotantes)
        print("✅ Adotante cadastrado com sucesso!")

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
        salvar_dados(path_ongs, ongs)
        print("✅ ONG cadastrada com sucesso!")

    elif escolha == '4':
        print("\nONGs cadastradas:")
        for ong in ongs:
            print(f"- {ong['nome']} | Local: {ong['localizacao']} | Contato: {ong['contato']} | Missão: {ong['missao']}")

    elif escolha == '5':
        print("\nAnimais cadastrados:")
        for i, animal in enumerate(animais, 1):
            print(f"{i}. {animal['especie']} {animal['raca']} ({animal['idade']} anos) - {animal['personalidade']}")
            print(f"   Histórico médico: {animal['historico_medico']}")

    elif escolha == '6':
        print("\nAdotantes cadastrados:")
        for i, adotante in enumerate(adotantes, 1):
            preferencias = ', '.join(adotante['preferencias'])
            print(f"{i}. {adotante['nome']} ({adotante['idade']} anos) - Preferências: {preferencias} | Estilo de vida: {adotante['estilo_vida']}")

    elif escolha == '7':
        print("\nAnimais cadastrados:")
        for i, animal in enumerate(animais, 1):
            print(f"{i}. {animal['especie']} {animal['raca']}")
        try:
            index = int(input("Digite o número do animal a excluir: ")) - 1
            if 0 <= index < len(animais):
                animais.pop(index)
                salvar_dados(path_animais, animais)
                print("✅ Animal excluído com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

    elif escolha == '8':
        print("\nAdotantes cadastrados:")
        for i, adotante in enumerate(adotantes, 1):
            print(f"{i}. {adotante['nome']}")
        try:
            index = int(input("Digite o número do adotante a excluir: ")) - 1
            if 0 <= index < len(adotantes):
                adotantes.pop(index)
                salvar_dados(path_adotantes, adotantes)
                print("✅ Adotante excluído com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

    elif escolha == '9':
        print("\nONGs cadastradas:")
        for i, ong in enumerate(ongs, 1):
            print(f"{i}. {ong['nome']}")
        try:
            index = int(input("Digite o número da ONG a excluir: ")) - 1
            if 0 <= index < len(ongs):
                ongs.pop(index)
                salvar_dados(path_ongs, ongs)
                print("✅ ONG excluída com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

    elif escolha == '10':
        print("👋 Saindo do sistema. Até mais!")
        sys.exit()

    else:
        print("❌ Opção inválida. Tente novamente.")
