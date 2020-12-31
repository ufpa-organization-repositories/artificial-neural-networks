# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Funcao de ativacao sigmoide
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

# Derivada da funcao de ativaçao sigmoide
def sigmoidDerivada(sig):
    return sig * (1 - sig)

def plotErrors(error_array):
    n_erros = error_array.__len__()
    x = np.linspace(1, n_erros, n_erros)
    y = [error for error in error_array]
    plt.plot(x, y, color='black')

    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.savefig('ErroMedio')
    plt.show()


def plotErrors_comparative(camadaSaida, saidas):
    x = np.linspace(1, len(saidas), len(saidas))
    y_obtido = []
    for obtido in camadaSaida:
        y_obtido.append(np.argmax(obtido) + 1)

    plt.scatter(x=x, y=y_obtido, color='red', label='Predicted Salary')
    plt.legend()

    y_esperado = []
    for saida in saidas:
        print(np.argmax(saida) + 1)
        y_esperado.append(np.argmax(saida) + 1)

    print(y_esperado)
    plt.scatter(x=x, y=y_esperado, color='white', edgecolors='black', label='Esperado')
    plt.legend()

    plt.title('1 = salário menor que 5000\n2 = salário maior ou igual a 5000')
    plt.xlabel('Exemplo')
    plt.ylabel('Salário')
    plt.savefig('Comparativo_esperado_obtido')
    plt.show()

def plotPrediction(camadaSaida):
    x = np.linspace(1, len(camadaSaida), len(camadaSaida))
    y_obtido = []
    for obtido in camadaSaida:
        y_obtido.append(np.argmax(obtido) + 1)

    plt.scatter(x=x, y=y_obtido, color='black')
    plt.legend()

    plt.xlabel('Vacancie')
    plt.ylabel('Salary (x1000)')
    plt.savefig('PredictionMLP')
    plt.show()


def train_backpropagation(epocas, entradas, pesos0, saidas, pesos1, taxaAprendizagem, momento):

    error_array = []
    camadaSaida = np.zeros([epocas])

    for epoca in range(epocas):

        """
        Feetfoward
        """
        camadaEntrada = entradas
        somaSinapse0 = np.dot(camadaEntrada, pesos0) + 1
        camadaOculta = sigmoid(somaSinapse0)

        somaSinapse1 = np.dot(camadaOculta, pesos1) + 1
        camadaSaida = sigmoid(somaSinapse1)

        """
        Backpropagation
        """

        erroCamadaSaida = (saidas - camadaSaida)
        mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
        error_array.append(mediaAbsoluta)

        print("Epoca: {}\tErro{}: ".format(epoca, mediaAbsoluta))

        derivadaSaida = sigmoidDerivada(camadaSaida)
        deltaSaida = erroCamadaSaida * derivadaSaida

        pesos1Transposta = pesos1.T
        deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
        deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)

        camadaOcultaTransposta = camadaOculta.T
        pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
        pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)

        camadaEntradaTransposta = camadaEntrada.T
        pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
        pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)

    # plotErrors(error_array)

    return pesos0, pesos1, camadaSaida, error_array

def apply_backpropagation(entradas, pesos0, pesos1, error_array):

    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0) + 1
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, pesos1) + 1
    camadaSaida = sigmoid(somaSinapse1)
    print('\nRESULTADO\n', '-' * 30)
    print(camadaSaida)

    for elem in camadaSaida:
        print(elem, np.round(elem))

    return camadaSaida


# n_neuronios_camadaOculta = 3
# epocas =10000
# taxaAprendizagem = 0.5
# momento = 1
#
# entradas = np.array([[0, 0],
#                      [0, 1],
#                      [1, 0],
#                      [1, 1]])
# n_entradas = entradas[0].__len__()
#
# saidas = np.array([[0], [1], [1], [0]])
# n_saidas = saidas[0].__len__()
#
# # camadaSaida = np.zeros([epocas])
#
# pesos0 = 2 * np.random.random((n_entradas, n_neuronios_camadaOculta)) - 1
# pesos1 = 2 * np.random.random((n_neuronios_camadaOculta, n_saidas)) - 1
#
# pesos0, pesos1, camadaSaida, error_array = train_backpropagation(epocas=epocas,
#                                                           entradas=entradas, pesos0=pesos0,
#                                                           saidas=saidas, pesos1=pesos1,
#                                                           taxaAprendizagem=taxaAprendizagem, momento=momento)
#
# apply_backpropagation(entradas=entradas, pesos0=pesos0,
#                       pesos1=pesos1,
#                       error_array=error_array)