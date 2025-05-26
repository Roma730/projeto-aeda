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