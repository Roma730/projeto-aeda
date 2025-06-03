import json
import os 
import sys

animais = []
ongs = []
adotantes = []
# Escolha dos usuários 
while True:
    print("=== Plataforma de Adoção de Animais ===")
    print("1- adicionar animal ")
    print("2- Lista de animais")
    
#add animais 
    escolha = input("escolha uma opção:")
    if escolha == '1':
        especie = input("especie: ")
        raca = input("raça: ")
        idade = input("idade: ")
        personalidade = input("personalidade: ")
        historico_medico = input("historico medico:")
        
        animal = {
            "especie": especie,
            "raca": raca,
            "idade": idade,
            "personalidade": personalidade,
            "historico_medico": historico_medico,
        }
        animais.append(animal)
        print("cadastro do animal realizado com sucesso!")
       
    elif escolha =="2":
            print("Lista de Animais:")
            contador = 1
            for animal in animais:
                print(f"especie: {animal['especie']},\nraça: {animal['raca']},\nidade: {animal['idade']},\npersonalidade: {animal['personalidade']},\nhistorico medico: {animal['historico_medico']}")
                
                contador +=1
        