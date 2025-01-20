import random
import timeit

# Тестування вбудованого сортування Python (Timsort)
if __name__ == "__main__":
    array_size = 10_000  # Розмір масиву
    test_data = [random.randint(0, 100_000) for _ in range(array_size)]  # Випадковий масив

    # Вимірювання часу виконання
    execution_time = timeit.timeit(lambda: sorted(test_data), number=1)
    print(f"Timsort (вбудована sorted): час виконання для масиву з {array_size} елементів: {execution_time:.4f} секунд")

# Отриманий результат: 
# Timsort (вбудована sorted): час виконання для масиву з 100000 елементів: 0.0119 секунд 
# Timsort (вбудована sorted): час виконання для масиву з 10000 елементів: 0.0009 секунд