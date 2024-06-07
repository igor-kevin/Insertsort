def insert_sort(desordenado: list):
    tamanho: int = len(desordenado)
    comparando: int
    for proximo in range(1, tamanho):
        comparando = desordenado[proximo]
        index_vetor: int = proximo

        # Enquanto estiver dentro do vetor e os valores forem maior do que o atual volta um no index
        while (index_vetor > 0 and desordenado[index_vetor-1] > comparando):
            desordenado[index_vetor] = desordenado[index_vetor-1]
            index_vetor -= 1

        desordenado[index_vetor] = comparando
        print('Valor comparado: ', comparando, 'Index: ',
              index_vetor, '\nVetor: ', desordenado)


if __name__ == "__main__":
    des = [9, 20, 17, 10, 18, 25, 25, 15, 2, 15, 17, 17, 16, 11, 3, 11, 25, 16, 12, 22, 24, 14, 8, 16, 21, 27, 27, 18, 1, 29, 16, 10, 0, 2, 2, 26, 19, 9, 12, 24, 20, 3, 16, 4, 4, 11, 9, 21, 25,
           6, 25, 10, 29, 20, 17, 23, 3, 26, 0, 30, 4, 20, 7, 11, 11, 19, 21, 4, 24, 13, 9, 29, 10, 22, 6, 28, 29, 28, 22, 10, 17, 3, 1, 1, 18, 2, 3, 11, 12, 28, 28, 7, 30, 25, 17, 28, 21, 12, 5, 12]
    print("Unsorted: ", des)

    insert_sort(des)

    print(des)
