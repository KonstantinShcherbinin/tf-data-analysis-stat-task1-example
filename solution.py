import pandas as pd
import numpy as np


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    error = -31.282
    acceleration = []
    for i in range(len(x) - 1):
        acceleration.append((x[i + 1] - x[i] + error*2)/10)

    return np.mean(acceleration) # Ваш ответ
