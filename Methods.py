import random
import time


class SortMethods:
    def __init__(self, total_numbers):
        self.total_numbers = total_numbers

    # Preenchendo Vetor Desordenado
    def fill_vector_disorder(self):
        vector = list(range(0, self.total_numbers + 1))
        random.shuffle(vector)
        return vector

    def shell_sort(self):
        vector = self.fill_vector_disorder()
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


print('Criado por Donald Shell em 1959, o método ShellSort é considerado um refinamento do método Insertion Sort.')
print('Ao invés de considerar o vetor a ser ordenado como um único segmento, ele divide o vetor em sub-grupos.')
print('Geralmente divide-se o tamanho do vetor ao meio e guarda o valor em uma variável h,'
      ' os grupos vão sendo ordenados, decrementando o valor de h até que os saltos sejam de elemento em elemento')
print('O gif a seguir ilustra bem o ShellSort')



order = SortMethods(10000)
before = time.time()
v = order.shell_sort()
after = time.time()  # Medindo o tempo
total = (after - before) * 1000  # Segundos multiplicados em 10000


print("O tempo gasto foi: {:6f} mili-segundos". format(total))
