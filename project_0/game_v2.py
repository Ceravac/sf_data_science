"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101)  #создаем загадываемое число в диапазоне
    count = 0
    low = 1 # минимальное значение шкалы
    high = 101 # максимальное значение шкалы
    while True:
        count += 1 # число попыток +1
        number = (low + high) // 2 #середина диапазона чисел
        
        if number == predict_number:
            break  # выход из цикла если угадал
        
        elif number < predict_number:
            # Если загаданное число больше предполагаемого, устанавливаем новый мин диапазон
            low = number + 1
        else: 
            # Если загаданное число меньше предполагаемого, устанавливаем новый макс диапазон
            high = number -1
                     
            #break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
