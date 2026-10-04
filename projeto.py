# item A
from datetime import datetime
def cadastro():
    while True:

        registro = ()
        print("=====Cadastro de veículo=====")

        try:
            modelo = input("Qual o modelo do veículo? ")

            ano_atual = datetime.now().year
            ano = int(input("Qual o ano do veículo? (ex: 2026): "))
            if ano < 1884 or ano > ano_atual:
                raise Exception("Escreva um ano válido")
           
            km = float(input("Quantos quilometros rodados?: "))
            if km < 0:
                raise Exception("Escreva uma quilometragem válida!")
         
            regitro = modelo, ano, km
            print(f"\nO veículo foi registrado!\nVeículo: {modelo} | Ano: {ano} | KM: {km}\n")

        except ValueError:
            print("Digite apenas números!\n")

        except Exception as erro:
            print(f"Opa! Algo deu errado!\n{erro}\n")

        if modelo == 'sair':
            break



# item B
def quilometragem(km, l):
    media = km/l
    print(f"Sua média de consumo de combustível foi de {media} KM/L.")
    escolha = int(input("Digite qual o combustível usado, 1 para gasolina e 2 para etanol: "))
    if escolha == 1:
        if media > 14:
            print("Veículo de alta eficiência, por ter um rendimento maior ou igual a 14 km/l com gasolina.")
        elif media >= 10 and media < 14:
            print("Veículo de desempenho moderado, por ter um rendimento entre 10 e 13,9 km/l com gasolina.")
        else:
            print("Veículo de alto consumo crítico, por ter um rendimento abaixo de 9,5 km/l com gasolina.")
    else:
        if media >= 10:
            print("Veículo de alta eficiência, por ter um rendimento maior ou igual 10 km/l com etanol.")
        elif media > 7.5 and media < 9.9:
            print("Veículo de desempenho moderado, por ter um rendimento entre 7,5 e 9,9 km/l com etanol.")
        else:
            print("Veículo de alto consumo crítico, por ter um rendimento abaixo de 7 km/l com etanol.")
# quilometros = float(input("Digite os quilometros rodados: "))
# litros = float(input("Digite os litros de gasolina consumidos: "))
# quilometragem(quilometros, litros)



# item C
reabastecimento = []
def registroCustos():
    tetoGastos = float(input("Digite o teto de gastos para abastecimentos desse mês: "))
    quaisPassaram = []
    quantidadePrecos = 0
    for i in reabastecimento:
        if i > tetoGastos:
            quantidadePrecos += 1
            quaisPassaram.append(i)
    print(f"{quantidadePrecos} passaram do teto de gastos de R$ {tetoGastos} para reabastecimentos, sendo eles: {quaisPassaram}")
# registroCustos()

            

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
# rotas ()



# item E
def faturamento():
    mesesCom31Dias = ['janeiro','março','maio','julho','agosto','outubro','dezembro']
    mesesCom30Dias = ['abril','junho','setembro','novembro']
    faturamento = []
    escolhaMes = input("Digite o mês que deseja registrar o faturamento: ").lower()
    if escolhaMes in mesesCom31Dias:
        for i in range(1,32):
            valor = float(input(f"Digite o faturamento do {i}º dia: "))
            faturamento.append(valor)
    elif escolhaMes in mesesCom30Dias:
        for i in range(1,31):
            valor = float(input(f"Digite o faturamento do {i}º dia: "))
            faturamento.append(valor)
    elif escolhaMes == 'fevereiro':
        for i in range(1,32):
            valor = float(input(f"Digite o faturamento do {i}º dia: "))
            faturamento.append(valor)
    else:
        print("Mês inválido")
        return
    totalFatura = sum(faturamento)
    mediaFatura = totalFatura/len(faturamento)
    maiorFatura = max(faturamento)
    menorFatura = min(faturamento)
    print(f"O faturamento total do mês foi de R$ {totalFatura}")
    print(f"A média de faturamento diário foi de R$ {mediaFatura}")
    print(f"O maior faturamento diário registrado no mês foi de R$ {maiorFatura}")
    print(f"O menor faturamento diário registrado no mês foi de R$ {menorFatura}")
# faturamento()



# item F
def processamentoDespesas(x):
    custosManutencao = []
    quantDesp = int(input("Digite a quantidade de despesas de manutenção da frota do período: "))
    for i in range(quantDesp):
        vlrDesp = float(input("Digite o valor da despesa de manutenção: "))
        custosManutencao.append(vlrDesp)
    mediaDespesas = sum(custosManutencao)/len(custosManutencao)

    quaisPassaramVlr = []
    for i in custosManutencao:
        if i > mediaDespesas:
            quaisPassaramVlr.append(i)
    print(quaisPassaramVlr)
# processamentoDespesas(custosmanutencao)




# item G
def main():
    while True:
        print(' \n \n Olá! \n 1 - Validação de Dados Cadastrais de Novo Veículo \n 2 - Cálculo de Rendimento Médio e Eficiência  \n 3 - Cálculo do Orçamento de Abastecimento \n 4 - Rotas \n 5 - Cálculo de Faturamento \n 6 - Processamento de Despesas \n 0 - Sair \n')
        try:
            opcoes = int(input('Digite a opção correspondente ao que deseja realizar no sistema: '))
            if opcoes == 1:
                cadastro()
            elif opcoes == 2:
                quilometros = float(input("Digite os quilometros rodados: "))
                litros = float(input("Digite os litros de gasolina consumidos: "))
                quilometragem(quilometros, litros)
            elif opcoes == 3:
                registroCustos()
            elif opcoes == 4:
                rotas()
            elif opcoes == 5:
                faturamento()
            elif opcoes == 6:
               custosManutencao = []
               processamentoDespesas(custosManutencao)
            elif opcoes == 0:
                print("Até breve!!!")
                break
            else:
                print("Digite uma opção válida por favor!")
        except ValueError:
            print("Digite apenas números por favor!")
        except Exception as erro:
            print(f"Opa! Algo deu errado!\n{erro}\n")
main()