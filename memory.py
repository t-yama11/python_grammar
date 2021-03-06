"""
メモリの使用量が気になったため, 変数のメモリ使用量を表示する.

そもそもメモリとは?
→ CPUが処理するデータを一時的に保存しておく場所. それに対して, 恒久的に
  保存しておく場所をHDDと言う.
  
変数オブジェクトのタイプとアドレスが表示された.
しかし, メモリ使用量はなぜか表示されない.

参考サイト
https://qiita.com/kpasso1015/items/83062ac14c3c44907e5b
"""

import numpy as np

if __name__ == "__main__":
    tmp = range(10000)
    print("mem: {}".format(tmp.__sizeof__))

    tmp = np.random.randn(1000,3)
    print("mem: {}".format(tmp.__sizeof__))
