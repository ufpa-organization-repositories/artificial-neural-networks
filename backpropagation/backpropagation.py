# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Funcao de ativacao sigmoide
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

# Derivada da funcao de ativaçao sigmoide
def sigmoidDerivada(sig):
    return sig * (1 - sig)


# Entradas
entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

# Saidas
saidas = np.array([[0], [1], [1], [0]])

# Inicializa os pesos da camada de entrada
pesos0 = 2 * np.random.random((2, 3)) - 1

# Pesos da camada oculta
pesos1 = 2 * np.random.random((3, 1)) - 1

epocas = 50000
taxaAprendizagem = 0.5
momento = 1

error_array = np.zeros(epocas)

for j in range(epocas):

    """
    Feetfoward
    """
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0) + 1 #bias       #Neuronios da camada oculta: soma das entradas ponderada pelos pesos
    camadaOculta = sigmoid(somaSinapse0)                #Neuronios da camada oculta: calcula a funcao de ativacao para cada neuronio

    somaSinapse1 = np.dot(camadaOculta, pesos1) + 1       #Neuronios da camada de saida: soma das entradas da camada de saida ponderada pelos pesos
    camadaSaida = sigmoid(somaSinapse1)                 #Neurônios da camada de saída: calculoo da funcao de ativacao para cada neuronio

    """
    Backpropagation
    """

    erroCamadaSaida = (saidas - camadaSaida)                                #Calcula o Erro
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))                        #Calcula o erro medio

    error_array[j] += mediaAbsoluta
    print("Epoca: {}\tErro{}: ".format(j, mediaAbsoluta))

    derivadaSaida = sigmoidDerivada(camadaSaida)                            #Calcula a derivada da funcao de ativacao
    deltaSaida = erroCamadaSaida * derivadaSaida                            #Calcula o delta da camada de saida

    pesos1Transposta = pesos1.T
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)     #Calcula o delta da camada oculta

    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)                     #Calcula os pesos da camada oculta
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)           #Atualiza os pesos da camada oculta

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)             #Calcula os pesos da camada de entrada
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)           #Atualiza os pesos da camada de entrada

#Teste
camadaEntrada = entradas
somaSinapse0 = np.dot(camadaEntrada, pesos0) + 1    #Neuronios da camada oculta: soma das entradas ponderada pelos pesos
camadaOculta = sigmoid(somaSinapse0)                #Neuronios da camada oculta: calcula a funcao de ativacao para cada neuronio

somaSinapse1 = np.dot(camadaOculta, pesos1) + 1    #Neuronios da camada de saida: soma das entradas da camada de saida ponderada pelos pesos
camadaSaida = sigmoid(somaSinapse1)

print(np.round(camadaSaida))

print(error_array)
x = np.linspace(1,epocas,epocas)
y = [error for error in error_array]
plt.plot(x, y)
plt.title('Erro médio x época')
plt.xlabel('Época')
plt.ylabel('Erro médio')
plt.savefig('ErroMedio')
plt.show()
