#!/usr/bin/env python3
import time
from botConfig import get_url, get_updates, get_json_from_url, get_last_update_id, send_message
from searchMethods import simple_sequence_search, sentry_sequence_search, jump_search, interpolation_search, binary_search
from searchMethods import fill_vector_order, fill_vector_disorder
from searchMethods import plotting_graph, compare_graph, search, compare_search
from sortMethods import*
import telegram
import db

TOKEN = "644291660:AAE0TNc6nMu4i-eky-5ASn__qJ26kgB63Xg"
bot = telegram.Bot(TOKEN)


def identify(list_aux):
    one = "BSS"
    two = "BSCS"
    three = "BB"
    four = "BPS"
    five = "BPI"
    new_list = []
    for search in list_aux:
        if search == one:
            aux = simple_sequence_search
            new_list.append(aux)
        elif search == two:
            aux = sentry_sequence_search
            new_list.append(aux)
        elif search == three:
            aux = binary_search
            new_list.append(aux)
        elif search == four:
            aux = jump_search
            new_list.append(aux)
        elif search == five:
            aux = interpolation_search
            new_list.append(aux)
    return new_list


def print_search(list_aux):
    one = "BSS"
    two = "BSCS"
    three = "BB"
    four = "BPS"
    five = "BPI"
    new_list = []
    for search in list_aux:
        if search == one:
            aux = "Busca Sequencial Simples"
            new_list.append(aux)
        elif search == two:
            aux = "Busca Sequencial Com Sentinela"
            new_list.append(aux)
        elif search == three:
            aux = "Busca Binária"
            new_list.append(aux)
        elif search == four:
            aux = "Busca Por Salto"
            new_list.append(aux)
        elif search == five:
            aux = "Busca Por Interpolação"
            new_list.append(aux)
    return new_list


def handle_updates(updates):
    # andando no json para para chegar no text enviado
    for update in updates["result"]:
        if 'message' in update:
            message = update['message']
        elif 'edited_message' in update:
            message = update['edited_message']
        else:
            print('Can\'t process! {}'.format(update))
        # pega o valor da mensagem mandada para o bot e a quebra
            return
        command = message["text"].split(" ", 1)[0]
        print(command)
        msg = ''
        chat = message["chat"]["id"]

        if len(message["text"].split(" ", 1)) > 1 and len(message["text"].split(" ")) == 3:
            try:
                msg = message["text"].split(" ", 1)[1].strip()
                positions = msg.split(" ")[0].strip()
                number = msg.split(" ")[1].strip()
            except:
                return send_message('Somente um argumento foi passado para o calculo da busca', chat)
        elif (len(message["text"].split(" ")) == 2):
            msg = message["text"].split(" ", 1)[1].strip()
            print(msg)
        if command == '/Buscas':
            send_message("*-------> Busca Sequencial Simples(BSS)*\n*-------> Busca Sequencial Com Sentinela(BSCS)*\n*-------> Busca Sequencial Indexada(BSI)*\n*-------> Busca Binária(BB)*\n*-------> Busca Por Salto(BPS)**\n*-------> Busca Por Interpolaçao(BPS)*", chat)
            send_message(
                " Digite '/' a sigla entre parentêses da busca \n ex:*/BSS* (Busca Sequencial Simples)", chat)
            send_message(
                " Caso queira comparar uma busca com a outra basta inserir um @ entre as buscas,por exemplo", chat)
        elif command == '/BSS':
            search(simple_sequence_search, positions,
                   number, 'Busca Sequencial Simples', chat)

            # print('telegram')
        elif command == '/BSCS':
            try:
                search(sentry_sequence_search, positions, number,
                       'Busca Sequencial Com Sentinela', chat)

            except:
                send_message('argumentos inválidos', chat)
        elif command == '/BB':
            try:
                search(binary_search, positions, number, 'Busca Binária', chat)

            except:
                send_message('argumentos inválidos', chat)
        elif command == '/BPS':
            try:

                search(jump_search, positions, number, 'Busca por Salto', chat)

            except:
                send_message('argumentos inválidos', chat)

        elif command == '/BPI':
            try:
                search(interpolation_search, positions,
                       number, 'Busca por Interpolação', chat)

            except:
                send_message('argumentos inválidos', chat)

        elif command == '/BSS@BSCS' or command == '/BSCS@BSS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)

        elif command == '/BSS@BB' or command == '/BB@BSS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BSS@BPI' or command == '/BPI@BSS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BSS@BPS' or command == '/BPS@BSS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BSCS@BB' or command == '/BB@BSCS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BSCS@BPS' or command == '/BPS@BSCS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BSCS@BPI' or command == '/BPI@BSCS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BB@BPI' or command == '/BPI@BB':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BB@BPS' or command == '/BPS@BB':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")

        elif command == '/BPS@BPI' or command == '/BPI@BPS':
            try:
                b = command
                b_n = b.replace("@", " ")
                b_new = b_n.replace("/", " ")
                search_list = b_new.split()
                list_names = print_search(search_list)
                list_identify = identify(search_list)

                first_time = compare_search(
                    list_identify[0], positions, number, list_names[0], chat)
                second_time = compare_search(
                    list_identify[1], positions, number, list_names[1], chat)
                compare_graph(first_time, second_time)
                bot.send_photo(chat_id=chat, photo=open(
                    './compare_methods.png', 'rb'))
                if first_time > second_time:
                    eficiencia = (first_time/second_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[1], int(eficiencia), list_names[0]), chat)
                elif first_time < second_time:
                    eficiencia = (second_time/first_time)
                    send_message('A {} foi {} vezes mais rápida que a {}'.format(
                        list_names[0], int(eficiencia), list_names[1]), chat)
            except:
                return send_message('OPS.... algum argumento foi passado errado,tente novamente', chat)
            # print("passa")
        elif command == '/SS':
            send_message(
                'Criado por Donald Shell em 1959, o método ShellSort é considerado um refinamento do método Insertion Sort.', chat)
            send_message(
                'Ao invés de considerar o vetor a ser ordenado como um único segmento, ele divide o vetor em sub-grupos.', chat)
            send_message('Geralmente divide-se o tamanho do vetor ao meio e guarda o valor em uma variável h os grupos vão sendo ordenados, decrementando o valor de h até que os saltos sejam de elemento em elemento', chat)
            send_message('O gif a seguir ilustra bem o ShellSort', chat)
            vector = fill_vector_disorder(int(msg))
            before = time.time()
            shell_sort(vector)
            after = time.time()
            total = (after - before) * 1000
            return send_message("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total), chat)

        elif command == '/QS':
            send_message(
                'O QuickSort é um algoritmo que aplica o conceito de dividir e conquistar.', chat)
            send_message(
                'Para particionar um vetor, escolhe-se um elemento pivô e move-se todos os valores menores para a esquerda e os maiores para a direita', chat)
            send_message(
                'Ordena-se recursivamente os valores menores e os maiores,O gif a seguir ilustra bem o QuickSort', chat)
            vector = fill_vector_disorder(int(msg))
            before = time.time()
            quicksort(vector)
            after = time.time()
            total = (after - before) * 1000
            return send_message("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total), chat)
        elif command == '/BS':
            send_message(
                'O BucketSort é um algoritmo que aplica o conceito de dividir e conquistar.', chat)
            send_message('Vamos particionar o vetor em um número finitos de baldes. Cada balde é ordenado individualmente, por diferentes algoritmos ou usando o bucket sort recursivamente', chat)
            send_message('imagem buccketSort', chat)
            send_message('É eficiente em dados cujos valores são limitados. Na nossa implementação cada balde foi ordenado usando o método insertion sort. Relembre através desse gif:', chat)
            vector = fill_vector_disorder(int(msg))
            before = time.time()
            bucket_sort(vector)
            after = time.time()
            total = (after - before) * 1000
            return send_message("O tempo gasto para ordenar o vetor foi: {:6f} mili-segundos". format(total), chat)


def main():
    last_update_id = None

    while True:
        print("Updates")
        updates = get_updates(last_update_id)

        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)

        time.sleep(0.3)


if __name__ == '__main__':
    main()
