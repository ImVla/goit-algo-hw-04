def insertion_sort(arr):
    """
    Функція сортування вставками.
    :param arr: Список, який потрібно відсортувати.
    :return: Відсортований список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Функція сортування злиттям.
    :param arr: Список, який потрібно відсортувати.
    :return: Відсортований список.
    """
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        sorted_arr = []
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
        sorted_arr.extend(left or right)
        return sorted_arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


import random
import timeit

def generate_data(size, data_type='random'):
    """
    Генерує список випадкових, відсортованих, чи зворотньо відсортованих елементів.
    :param size: Розмір списку.
    :param data_type: Тип даних у списку ('random', 'sorted', 'reversed').
    :return: Список даних.
    """
    random_data = [random.randint(1, 1000) for _ in range(size)]
    if data_type == 'sorted':
        return sorted(random_data)
    elif data_type == 'reversed':
        return sorted(random_data, reverse=True)
    return random_data

def benchmark_sorting_algorithms(data, number=1):
    """
    Вимірює час виконання різних алгоритмів сортування.
    :param data: Дані для сортування.
    :param number: Кількість повторень для кожного вимірювання.
    :return: Словник з часами виконання для кожного алгоритму.
    """
    times = {}

    # Тестування сортування вставками
    times['insertion_sort'] = timeit.timeit(
        'insertion_sort(data.copy())', globals=globals(), number=number)

    # Тестування сортування злиттям
    times['merge_sort'] = timeit.timeit(
        'merge_sort(data.copy())', globals=globals(), number=number)

    # Тестування Timsort (використання вбудованої функції sorted)
    times['timsort'] = timeit.timeit(
        'sorted(data.copy())', globals=globals(), number=number)

    return times


# Розміри наборів даних для тестування
data_sizes = [100, 1000, 10000]
data_types = ['random', 'sorted', 'reversed']

# Словник для зберігання результатів
benchmark_results = {size: {dtype: None for dtype in data_types} for size in data_sizes}

# Запуск тестувань
for size in data_sizes:
    for dtype in data_types:
        data = generate_data(size, data_type=dtype)
        result = benchmark_sorting_algorithms(data, number=1)
        benchmark_results[size][dtype] = result

benchmark_results
