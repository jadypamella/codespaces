def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def test_bubble_sort():
    # Teste para uma lista não ordenada
    unsorted_list = [5, 2, 8, 6, 1, 3, 9, 4, 7]
    bubble_sort(unsorted_list)
    assert unsorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9], print("Erro: {unsorted_list}")

    # Teste para uma lista já ordenada
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bubble_sort(sorted_list)
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Erro: {sorted_list}"

    # Teste para uma lista com valores duplicados
    duplicated_list = [4, 2, 1, 4, 3, 2, 1]
    bubble_sort(duplicated_list)
    assert duplicated_list == [1, 1, 2, 2, 3, 4, 4], f"Erro: {duplicated_list}"

    # Teste para uma lista vazia
    empty_list = []
    bubble_sort(empty_list)
    assert empty_list == [], f"Erro: {empty_list}"

test_bubble_sort()
numbers = [10, 9, 5, 22, 1, 43]
result = bubble_sort(numbers)
print(result)
