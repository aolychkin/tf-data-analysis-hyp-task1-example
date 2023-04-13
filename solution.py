import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.07
    z_stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], value=0, alternative='smaller')
    z_crit = np.abs(norm.ppf(alpha))
    #print(f"Z_stat = {z_stat} \t Z_crit = {z_crit} \t P = {p_value}")
    if np.abs(z_stat) > z_crit:
        return True
    else:
        return False
