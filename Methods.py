import random
import time


    # Preenchendo Vetor Desordenado
def fill_vector_disorder(total_numbers):
    vector = list(range(0, total_numbers + 1))
    random.shuffle(vector)
    return vector


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


print('Criado por Donald Shell em 1959, o método ShellSort é considerado um refinamento do método Insertion Sort.')
print('Ao invés de considerar o vetor a ser ordenado como um único segmento, ele divide o vetor em sub-grupos.')
print('Geralmente divide-se o tamanho do vetor ao meio e guarda o valor em uma variável h,'
      ' os grupos vão sendo ordenados, decrementando o valor de h até que os saltos sejam de elemento em elemento')


print('O gif a seguir ilustra bem o ShellSort')



print('Agora vamos calcular o tempo que o algoritmo demora para ordenar um vetor.')
total_number = int(input('Digite a quantidade de elementos do vetor: '))

v = fill_vector_disorder(total_number)

before = time.time()
shel = shell_sort(v)
after = time.time()
total = (after - before) * 1000  # Segundos multiplicados em 10000
print("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total))

print('---------------------------------------------------------------------------------------------------------------')


print('O QuickSort é um algoritmo que aplica o conceito de dividir e conquistar.')
print('Para particionar um vetor, escolhe-se um elemento pivô e move-se todos os valores menores para a esquerda e os'
      'maiores para a direita')
print('Ordena-se recursivamente os valores menores e os maiores')



print('O gif a seguir ilustra bem o QuickSort')



print('Agora vamos calcular o tempo que o algoritmo demora para ordenar um vetor.')
total_number = int(input('Digite a quantidade de elementos do vetor: '))
v = fill_vector_disorder(total_number)

b = time.time()
quick = quicksort(v)
a = time.time()
t = (a - b) * 1000  # Segundos multiplicados em 10000
print("O tempo gasto foi: {:6f} mili-segundos". format(t))



