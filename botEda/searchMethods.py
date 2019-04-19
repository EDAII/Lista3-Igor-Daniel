import matplotlib.pyplot as plt
import tkinter
import numpy as np
import random
import math
import time
import db
from db import Busca
from botConfig import get_url,get_updates,get_json_from_url,get_last_update_id,send_message
import urllib
import telegram

TOKEN = "644291660:AAE0TNc6nMu4i-eky-5ASn__qJ26kgB63Xg"
bot = telegram.Bot(TOKEN)


def fill_vector_order_different(v):
    vector = list(range(0, v + 1))
    return vector

# Preenchendo Vetor Ordenado
def fill_vector_order(total_numbers):
    vector = list(range(0,total_numbers + 1))
    return vector
    
# Preenchendo Vetor Desordenado
def fill_vector_disorder(total_numbers):
    vector = list(range(0,total_numbers + 1))
    random.shuffle(vector)
    return vector

# Busca Sequencial Simples: Podemos trabalhar tanto com o vetor ordenado quanto desordenado
def simple_sequence_search(total_numbers,valor_a_ser_encontrado):
    vector = fill_vector_disorder(total_numbers)
    i = 0
    while i < len(vector):
        if vector[i] == valor_a_ser_encontrado:
            return i
        i += 1

    return -1

# Busca sequencial com Sentinela: Podemos trabalhar tanto com o vetor ordenado quanto desordenado
def sentry_sequence_search(total_numbers,valor_a_ser_encontrado):
    vector = fill_vector_order(total_numbers)
    i = 0
    vector.append(valor_a_ser_encontrado)
    while vector[i] != valor_a_ser_encontrado:
        i += 1
    if i == len(vector) - 1:
        return -1
    return  i
   
# Busca Binária: Os elementos devem está ordenados
def binary_search(total_numbers,valor_a_ser_encontrado):
    vector = fill_vector_order(total_numbers)
    left, right, attempt = 0, len(vector), 1
    while 1:
        middle = int((left + right) / 2)
        aux_num = vector[middle]
        if valor_a_ser_encontrado == aux_num:
            return attempt
        elif valor_a_ser_encontrado > aux_num:
            left = middle
        else:
            right = middle
        attempt += 1      
    return -1

# Busca por Interpolação: Os elementos devem está ordenados
def interpolation_search(total_numbers,valor_a_ser_encontrado):
    begin = 0
    vector = fill_vector_order(total_numbers)
    end = len(vector) - 1
    while begin <= end and vector[begin] <= valor_a_ser_encontrado <= vector[end]:
        i = int(begin + (((end - begin)/(vector[end] - vector[begin])) * (valor_a_ser_encontrado - vector[begin])))
        if vector[i] == valor_a_ser_encontrado:
            return "O elemento {} foi encontrado na posição {}".format(valor_a_ser_encontrado, i)
        if valor_a_ser_encontrado > vector[i]:
            begin = i + 1
        else:
            end = i - 1
    return -1

#  Função para plotar gráficos
def plotting_graph(total_time):
    x = np.linspace(0, total_time, 10)
    y = x
    plt.plot(x, y)
    plt.title('Time - Search Method')
    plt.xlabel('time(x 1000)')
    plt.ylabel('time(x 1000)')
    plt.savefig('method.png', bbox_inches='tight')
    #plt.show()

# Função para comparar gráficos
def compare_graph(total_time_one, total_time_two):
    x = np.linspace(0, total_time_one, 10)
    y = x
    x_2 = np.linspace(0, total_time_two, 10)
    y_2 = x_2
    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title('Time 1')
    plt.xlabel('time(x 1000)')
    plt.ylabel('time(x 1000)')
    plt.subplot(1, 2, 2)
    plt.plot(x_2, y_2, 'r')
    plt.title('Time 2')
    plt.xlabel('time(x 1000)')
    plt.ylabel('time(x 1000)')
    plt.savefig('compare_methods.png', bbox_inches='tight')
    #plt.show()
    

# Busca por salto: Similar a busca binária, funciona através de saltos
def jump_search(total_numbers,valor_a_ser_encontrado):
    lys = fill_vector_order(total_numbers)
    val = valor_a_ser_encontrado
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump
    if left >= length or lys[left] > val:
        return "Não foi possível encontrar o elemento {}".format(val)
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return "Não foi possível encontrar o elemento {}".format(val)

def search(search_method,positions,number,type_search,chat):
    inicio = time.time()
    posicao=search_method(int(positions),int(number))
    if posicao == -1:
        return send_message('Esse valor não está dentro do array selecionado',chat)
    else:
        fim = time.time()
        tempo = (fim-inicio)*1000
        busca = Busca(chat=chat, typeSearch=type_search, positions=int(positions),number=int(number),tempoExecucao=float(tempo))
        db.session.add(busca)
        db.session.commit()
        send_message("A {} levou *{:4f}* milisegundos para buscar o valor *{}* em um vetor de {} posições na posição *{}*".format(busca.typeSearch,busca.tempoExecucao,busca.number,busca.positions,posicao), chat)
        plotting_graph(tempo)
        bot.send_photo(chat_id=chat, photo=open('./method.png', 'rb'))
        return tempo

def compare_search(search_method,positions,number,type_search,chat):
    inicio = time.time()
    posicao=search_method(int(positions),int(number))
    if posicao == -1:
        return send_message('Esse valor não está dentro do array selecionado',chat)
    else:
        fim = time.time()
        tempo = (fim-inicio)*1000
        busca = Busca(chat=chat, typeSearch=type_search, positions=int(positions),number=int(number),tempoExecucao=float(tempo))
        db.session.add(busca)
        db.session.commit()
        send_message("A {} levou *{:4f}* milisegundos para buscar o valor *{}* em um vetor de {} posições na posição *{}*".format(busca.typeSearch,busca.tempoExecucao,busca.number,busca.positions,posicao), chat)
        return tempo