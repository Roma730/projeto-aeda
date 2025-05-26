import sys 

class ONG:
    def __init__(self,nome, endereco, telefone, email ,):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

        def __str__(self):
            return (
                f"Nome: {self.nome}\n"
                f"Endereço: {self.endereco}\n"
                f"telefone: {self.telefone}\n"
                f"email: {self.email}\n"
            )
        
class Animal:
    def __init__(self, nome, especie, raca, idade, personalidade, historico_medico):
        self.nome = nome
        self.especie = especie
        self.raca =raca 
        self.idade = idade
        self.personalidade = personalidade 
        self.historico_medico = historico_medico

        def __str__(self):
            peronalidade_str = ', '.join(self.personalidade) if self.personalidade else "N/A"
            return(
                f"Nome:{self.nome}\n"
                f"Espécie: {self.especie}\n"
                f"Raça" {self.raca}\n"
                f"idade: {self.idade} ano{'s' if self.idade != 1 else''}\n
                f"traços depersonalidade: {pesrsonalidade_str}"
                f"Historico médico: {self.historico_medico}\n"
            )
            