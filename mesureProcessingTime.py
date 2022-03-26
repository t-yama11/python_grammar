"""
wrapper関数の使い方に慣れる.
ここでは, wrapper関数を用いて関数の処理時間の表示を行う.
"""

import time


def measure_processing_time(func):
    """
    Parametar
    -------------------------------------------
    func : 処理時間計測の対象となる関数.

    Returns
    -------------------------------------------
    None : 関数funcの処理時間を表示する.

    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        _ = func(*args, *kwargs)
        end_time = time.perf_counter()
        print("{0} : {1} [s]".format(func.__name__, end_time-start_time))
    return wrapper


# 引数nで 1を加算する回数を指定する.
@measure_processing_time
def sample(n):
    a = 0
    
    for i in range(n):
        a += 1
    
    print(a)
    
if __name__ == "__main__":
    sample(1000**2)
