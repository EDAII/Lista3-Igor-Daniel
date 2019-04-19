import random
import time


    # Preenchendo Vetor Desordenado
def fill_vector_disorder(total_numbers):
    vector = list(range(0, total_numbers + 1))
    random.shuffle(vector)
    return vector


def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        insertion_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


def shell_sort(v):
    vector = v
    gap = len(vector) // 2
    while gap > 0:

        for i in range(gap, len(vector)):
            temp = vector[i]
            j = i
            # Sort the sub list for this gap

            while j >= gap and vector[j - gap] > temp:
                vector[j] = vector[j - gap]
                j = j - gap
            vector[j] = temp

        # Reduce the gap for the next element

        gap = gap // 2
    return vector


def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


# print('---------------------------------------------------------------------------------------------------------------')
# print('Criado por Donald Shell em 1959, o método ShellSort é considerado um refinamento do método Insertion Sort.')
# print('Ao invés de considerar o vetor a ser ordenado como um único segmento, ele divide o vetor em sub-grupos.')
# print('Geralmente divide-se o tamanho do vetor ao meio e guarda o valor em uma variável h,'
#       ' os grupos vão sendo ordenados, decrementando o valor de h até que os saltos sejam de elemento em elemento')


# print('O gif a seguir ilustra bem o ShellSort')



# print('Agora vamos calcular o tempo que o algoritmo demora para ordenar um vetor.')
# total_number = int(input('Digite a quantidade de elementos do vetor: '))

# v = fill_vector_disorder(total_number)

# before = time.time()
# shel = shell_sort(v)
# after = time.time()
# total = (after - before) * 1000  # Segundos multiplicados em 10000
# print("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total))

# print('---------------------------------------------------------------------------------------------------------------')


# print('O QuickSort é um algoritmo que aplica o conceito de dividir e conquistar.')
# print('Para particionar um vetor, escolhe-se um elemento pivô e move-se todos os valores menores para a esquerda e os'
#       'maiores para a direita')
# print('Ordena-se recursivamente os valores menores e os maiores')



# print('O gif a seguir ilustra bem o QuickSort')



# print('Agora vamos calcular o tempo que o algoritmo demora para ordenar um vetor.')
# total_number = int(input('Digite a quantidade de elementos do vetor: '))
# v = fill_vector_disorder(total_number)

# b = time.time()
# quick = quicksort(v)
# a = time.time()
# t = (a - b) * 1000  # Segundos multiplicados em 10000
# print("O tempo gasto foi: {:6f} mili-segundos". format(t))

# print('---------------------------------------------------------------------------------------------------------------')
# print('O BucketSort é um algoritmo que aplica o conceito de dividir e conquistar.')
# print('Vamos particionar o vetor em um número finitos de baldes. Cada balde é ordenado individualmente, por diferentes'
#       'algoritmos ou usando o bucket sort recursivamente.')



# print('IMAGEM BUCKET SORT')



# print('[É eficiente em dados cujos valores são limitados. Na nossa implementação cada balde foi ordenado usando o método'
#       'insertion sort. Relembre através desse gif:')



# print('GIF INSERTION SORT')




# print('Agora vamos calcular o tempo que o algoritmo demora para ordenar um vetor.')
# total_number = int(input('Digite a quantidade de elementos do vetor: '))

# v = fill_vector_disorder(total_number)
# bef = time.time()
# bucket = bucket_sort(v)
# aft = time.time()
# tot = (aft - bef) * 1000  # Segundos multiplicados em 10000
# print("O tempo gasto foi: {:6f} mili-segundos". format(tot))
# print('---------------------------------------------------------------------------------------------------------------')

