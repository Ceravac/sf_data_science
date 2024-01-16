<<<<<<< HEAD
"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
=======
import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))

>>>>>>> 4efc834 (Initial commi)
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")
<<<<<<< HEAD
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
=======

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла
>>>>>>> 4efc834 (Initial commi)
