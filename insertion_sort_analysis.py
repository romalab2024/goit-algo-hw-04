import random
import timeit

def insertion_sort(arr):
    """
    Реалізація алгоритму сортування вставками.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Тестування сортування вставками
if __name__ == "__main__":
    array_size = 50_000  # Розмір масиву (зменшено для сортування вставками, оскільки алгоритм повільний)
    test_data = [random.randint(0, 100_000) for _ in range(array_size)]  # Випадковий масив

    # Вимірювання часу виконання
    execution_time = timeit.timeit(lambda: insertion_sort(test_data), number=1)
    print(f"Сортування вставками: час виконання для масиву з {array_size} елементів: {execution_time:.4f} секунд")

#  Отриманий результат:   
# Сортування вставками: час виконання для масиву з 1_000 елементів: 0.0147 секунд
# Сортування вставками: час виконання для масиву з 10_000 елементів: 1.5667 секунд 
# Сортування вставками: час виконання для масиву з 50000 елементів: 45.4612 секунд