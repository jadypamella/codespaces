#Complexidade de tempo O(1) e complexidade espacial O(1):
def add_numbers(a, b):
    return a + b

#Complexidade de tempo O(n) e complexidade espacial O(1):
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

#Complexidade de tempo O(n) e complexidade espacial O(n):
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

#Complexidade de tempo O(n²) e complexidade espacial O(1):
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

#Complexidade de tempo exponencial O(n!)
def permutations(string):
    if len(string) == 1:
        return [string]
    perms = []
    for i, c in enumerate(string):
        for perm in permutations(string[:i] + string[i+1:]):
            perms.append(c + perm)
    return perms
	
'''O primeiro parâmetro len(string)-1 define o índice inicial da iteração, que é o índice do último caractere da string (a indexação em Python começa em 0). O segundo parâmetro -1 define o índice final da iteração, que é -1 porque queremos parar na posição anterior à primeira posição da string. O terceiro parâmetro -1 define o passo da iteração, que é -1 porque queremos percorrer a string de trás para frente, ou seja, decrementando os índices.

Usando esses parâmetros na função reverse_string, podemos iterar pelos índices da string de trás para frente e concatenar os caracteres em ordem inversa para obter a string reversa desejada. É uma forma simples e eficiente de realizar essa operação em Python.