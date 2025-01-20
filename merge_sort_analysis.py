import random
import timeit

def merge_sort(arr):
    """
    Реалізація алгоритму сортування злиттям.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Функція злиття двох відсортованих масивів.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Тестування сортування злиттям
if __name__ == "__main__":
    array_size = 10_000  # Розмір масиву
    test_data = [random.randint(0, 100_000) for _ in range(array_size)]  # Випадковий масив

    # Вимірювання часу виконання
    execution_time = timeit.timeit(lambda: merge_sort(test_data), number=1)
    print(f"Сортування злиттям: час виконання для масиву з {array_size} елементів: {execution_time:.4f} секунд")

#  Отриманий результат: 
# Сортування злиттям: час виконання для масиву з 100000 елементів: 0.2154 секунд 
# Сортування злиттям: час виконання для масиву з 10000 елементів: 0.0175 секунд