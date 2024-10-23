"""
Модуль для розв'язання задачі оптимального з'єднання мережевих кабелів.

Цей модуль надає функціонал для знаходження найбільш економічного способу
з'єднання мережевих кабелів різної довжини. Задача полягає в тому, щоб
знайти такий порядок попарного з'єднання кабелів, який мінімізує
загальні витрати на всі з'єднання.
"""


import heapq


def min_connection_cost(cables):
    """
    Функція для знаходження мінімальних витрат на з'єднання кабелів
    
    Args:
        cables (list): Список довжин кабелів
    
    Returns:
        tuple: (загальні витрати, список кроків з'єднання)
    """
   # Перевірка вхідних даних
    if not cables:
        raise ValueError("Список кабелів не може бути порожнім")
    if any(x < 0 for x in cables):
        raise ValueError("Довжини кабелів мають бути додатними числами")

    # Створюємо мінімальну купу з довжин кабелів
    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0  # Загальні витрати
    steps = []      # Список кроків з'єднання

    # Продовжуємо, поки в купі не залишиться один кабель
    while len(heap) > 1:
        # Беремо два найкоротші кабелі
        first_cable = heapq.heappop(heap)
        second_cable = heapq.heappop(heap)

        # Розраховуємо вартість з'єднання
        connection_cost = first_cable + second_cable

        # Додаємо крок до списку
        steps.append((first_cable, second_cable, connection_cost))

        # Додаємо вартість до загальних витрат
        total_cost += connection_cost

        # Додаємо новий з'єднаний кабель назад до купи
        heapq.heappush(heap, connection_cost)

    return total_cost, steps


# Приклад використання
if __name__ == "__main__":
    input_cables = [10, 7, 6, 21, 15, 4, 18]
    result_cost, result_steps = min_connection_cost(input_cables)

    print(f"Початкові довжини кабелів: {input_cables}")
    print("\nКроки з'єднання:")
    for i, (cable1, cable2, cost) in enumerate(result_steps, 1):
        print(f"Крок {i}: з'єднуємо кабелі довжиною {cable1} та {cable2}, вартість = {cost}")
    print(f"\nЗагальні витрати: {result_cost}")
