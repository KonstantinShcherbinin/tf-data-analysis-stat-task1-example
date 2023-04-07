import pandas as pd
import numpy as np


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    error = -31.282
    #acceleration = []
    #for i in range(len(x) - 1):
    #    acceleration.append((x[i + 1] - x[i])/10 + (2 / error))

    return 1 / np.mean([(i + error)/10 for i in x]) # Ваш ответ

#if __name__ == '__main__':
#    m = np.array([32, 33, 34, 32, 31])
#    res = solution(m)
#    print(res)
#    print(np.mean(sum([(i - res)**2 for i in m])))