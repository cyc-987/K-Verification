import random
from sympy import gcd, mod_inverse

# 输入两个大素数 p 和 q
p_all = [43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
q_all = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

for p in p_all:
    for q in q_all:
        print(f"p: {p}, q: {q}")

        # 计算 n 和 φ(n)
        n = p * q
        phi_n = (p - 1) * (q - 1)

        # 选择 e，使得 1 < e < φ(n) 且 gcd(e, φ(n)) = 1
        def find_e(phi_n):
            for e in range(10, 20):
                if gcd(e, phi_n) == 1:
                    return e
            return None

        e = find_e(phi_n)
        if e == None:
            print("No e found")
            continue

        # 计算 d，使得 ed ≡ 1 (mod φ(n))
        d = mod_inverse(e, phi_n)
        if d > 1500:
            print("d too large")
            continue

        # 输出公钥和私钥
        print(f"Pub(n,e): [{n}, {e}]")
        print(f"Pri(n,d): [{n}, {d}]")