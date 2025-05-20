from difflib import SequenceMatcher
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Animal:
    name: str
    species: str
    race: str
    age: int
    personality: str
    lifestyle: str
    medical_history: str


# Lista de animais disponíveis para adoção
animals: List[Animal] = [
    Animal("Luna", "Cachorro", "Vira-lata", 2, "Brincalhão", "Ativo", "Vacinado"),
    Animal("Mimi", "Gato", "Siamês", 3, "Calmo", "Tranquilo", "Castrado"),
    Animal("Thor", "Cachorro", "Labrador", 4, "Protetor", "Ativo", "Vacinado e Castrado"),
]


def match_animals(adopter: Dict[str, str], animal_list: List[Animal]) -> List[Animal]:
    """
    Calcula os melhores matches de animais para um adotante.
    """
    matches = []
    for animal in animal_list:
        score = 0
        if animal.species.lower() == adopter["preferred_species"].lower():
            score += 1
        if animal.personality.lower() == adopter["preferred_personality"].lower():
            score += 1
        score += SequenceMatcher(
            None, animal.lifestyle.lower(), adopter["lifestyle"].lower()
        ).ratio()
        matches.append((animal, score))
    
    matches.sort(key=lambda x: x[1], reverse=True)
    return [match[0] for match in matches[:3]]


def get_valid_input(prompt: str, valid_options: List[str]) -> str:
    """
    Solicita uma entrada do usuário e valida contra uma lista de opções.
    """
    while True:
        user_input = input(f"{prompt} {valid_options}: ").strip().capitalize()
        if user_input in valid_options:
            return user_input
        print(f"Entrada inválida. Escolha uma das opções: {valid_options}")


def get_adopter_input() -> Dict[str, str]:
    """
    Coleta dados do adotante com validação.
    """
    print("=== Bem-vindo ao sistema de adoção ===")
    preferred_species = get_valid_input("Espécie preferida", ["Cachorro", "Gato"])
    preferred_personality = get_valid_input("Personalidade desejada", ["Brincalhão", "Calmo", "Protetor"])
    lifestyle = get_valid_input("Seu estilo de vida", ["Ativo", "Tranquilo"])

    return {
        "preferred_species": preferred_species,
        "preferred_personality": preferred_personality,
        "lifestyle": lifestyle
    }


def show_matches(matches: List[Animal]) -> None:
    """
    Mostra os animais compatíveis com o adotante.
    """
    if not matches:
        print("Nenhum animal compatível encontrado.")
        return

    print("\nAnimais compatíveis com você:")
    for i, animal in enumerate(matches, 1):
        print(f"\n#{i} - {animal.name} ({animal.species})")
        print(f"Raça: {animal.race}")
        print(f"Idade: {animal.age} anos")
        print(f"Personalidade: {animal.personality}")
        print(f"Estilo: {animal.lifestyle}")
        print(f"Histórico médico: {animal.medical_history}")


def main() -> None:
    adopter = get_adopter_input()
    best_matches = match_animals(adopter, animals)
    show_matches(best_matches)


if __name__ == "__main__":
    main()
