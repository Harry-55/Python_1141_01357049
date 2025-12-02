import numpy as np
from scipy import linalg
import time

A = np.random.rand(200, 200)
B = np.random.rand(200, 200)


def manual_matmul(A, B):    
    C = np.zeros((200, 200))

    start_manual = time.perf_counter() 
    for i in range(200):
        for j in range(200):
            s = 0.0
            for k in range(200):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    manual_time = time.perf_counter() - start_manual
    return C, manual_time


C_manual , manual_time= manual_matmul(A, B)
# end_manual = time.time()

start_scipy = time.perf_counter()
C_scipy = linalg.blas.dgemm(1.0, A, B)
# end_scipy = time.time()
scipy_time = time.perf_counter() - start_scipy

is_close = np.allclose(C_manual, C_scipy)

print("自行實作矩陣乘法執行時間：", manual_time, "秒")
print("SciPy 加速矩陣乘法執行時間：", scipy_time, "秒")
print("兩者結果是否近似相同：", is_close)