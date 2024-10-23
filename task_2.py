"""
Модуль для злиття k відсортованих списків в один відсортований список
використовуючи мінімальну купу.
"""


import heapq


def merge_k_lists(lists):
    """
    Функція для злиття k відсортованих списків в один відсортований список.

    Args:
        lists (List[List[int]]): Список відсортованих списків цілих чисел

    Returns:
        List[int]: Об'єднаний відсортований список

    Приклад:
        >>> input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        >>> merge_k_lists(input_lists)
        [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not lists:
        return []

    # Видаляємо порожні списки
    lists = [lst for lst in lists if lst]
    if not lists:
        return []

    result = []
    # Створюємо мінімальну купу з перших елементів кожного списку
    # Зберігаємо кортежі (значення, індекс списку, позиція в списку)
    heap = []

    # Додаємо перший елемент кожного списку до купи
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))

    # Поки купа не порожня
    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        result.append(val)

        # Якщо в поточному списку ще є елементи, додаємо наступний
        if element_index + 1 < len(lists[list_index]):
            next_element_index = element_index + 1
            next_val = lists[list_index][next_element_index]
            heapq.heappush(heap, (next_val, list_index, next_element_index))

    return result


# Приклад використання
if __name__ == "__main__":
    input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(input_lists)
    print("Відсортований список:", merged_list)

    # Додаткові тести
    print("\nДодаткові тести:")

    # Тест 1: Порожні списки
    print("Тест з порожніми списками:",
          merge_k_lists([[], [], []]))

    # Тест 2: Один список
    print("Тест з одним списком:",
          merge_k_lists([[1, 2, 3]]))

    # Тест 3: Списки різної довжини
    print("Тест зі списками різної довжини:",
          merge_k_lists([[1], [1, 2, 3], [2]]))
