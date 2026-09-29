# from datetime import datetime

# while True:

#     registro = ()
#     print("=====Cadastro de veículo=====")

#     try:
#         modelo = input("Qual o modelo do veículo? ")

#         ano_atual = datetime.now().year
#         ano = int(input("Qual o ano do veículo? (ex: 2026): "))
#         if ano < 1884 or ano > ano_atual:
#             raise Exception("Escreva um ano válido")
           
#         km = float(input("Quantos quilometros rodados?: "))
#         if km < 0:
#             raise Exception("Escreva uma quilometragem válida!")
         
#         regitro = modelo, ano, km
#         print(f"\nO veículo foi registrado!\nVeículo: {modelo} | Ano: {ano} | KM: {km}\n")

#     except ValueError:
#         print("Digite apenas números!\n")

#     except Exception as erro:
#         print(f"Opa! Algo deu errado!\n{erro}\n")

#     if modelo == 'sair':
#         break

# item B
# def quilometragem(km, l):
#     media = km/l
#     print(f"Sua média de consumo de combustível foi de {media} KM/L.")
#     escolha = int(input("Digite qual o combustível usado, 1 para gasolina e 2 para etanol: "))
#     if escolha == 1:
#         if media > 14:
#             print("Veículo de alta eficiência, por ter um rendimento maior ou igual a 14 km/l com gasolina.")
#         elif media >= 10 and media < 14:
#             print("Veículo de desempenho moderado, por ter um rendimento entre 10 e 13,9 km/l com gasolina.")
#         else:
#             print("Veículo de alto consumo crítico, por ter um rendimento abaixo de 9,5 km/l com gasolina.")
#     else:
#         if media >= 10:
#             print("Veículo de alta eficiência, por ter um rendimento maior ou igual 10 km/l com etanol.")
#         elif media > 7.5 and media < 9.9:
#             print("Veículo de desempenho moderado, por ter um rendimento entre 7,5 e 9,9 km/l com etanol.")
#         else:
#             print("Veículo de alto consumo crítico, por ter um rendimento abaixo de 7 km/l com etanol.")
# quilometros = float(input("Digite os quilometros rodados: "))
# litros = float(input("Digite os litros de gasolina consumidos: "))
# quilometragem(quilometros, litros)

# item C
reabastecimento = [50.0, 120.0, 45.0, 68.32, 82.54, 54.00, 320.00, 400.00, 54.87, 10.00]
print("Tenha em mente que o teto de gastos com o reabastecimento é de R$ 300,00")
def registroCustos():
    for i in reabastecimento:



# item D
import numpy as np

def rotas():
    rotas = np.array([
        [120, 2, 25.00],
        [250, 3.5, 42.50],
        [80, 4.2, 15.00],
        [310, 1.2, 58.00]
    ])

    km = rotas[:, 0]
    tempo = rotas[:, 1]
    pedagio = rotas[:, 2]

    taxa_por_km = 2.50

    custo_total = (km * taxa_por_km) + pedagio


    # <8 formatação de texto
    print(f"{'Rota':<8} | {'KM':<8} | {'Tempo (h)':<10} | {'Pedágio (R$)':<12} | {'Custo Total (R$)':<15}")
    print("-" * 65)


    # =1 para cada rota lida
    for i in range(len(rotas)):
        print(f"Rota {i+1:<3} | {km[i]:<8.1f} | {tempo[i]:<10.1f} | R$ {pedagio[i]:<9.2f} | R$ {custo_total[i]:<12.2f}")

rotas ()