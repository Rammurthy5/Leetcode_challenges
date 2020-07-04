"""
Find kth factor of given number n

"""


def kthFactor(n: int, k: int) -> int:
    res = [1]

    for i in range(2, (n // 2)+1):
        if n % i == 0:
            res.append(i)
    res.append(n)
    if len(res) >= k:
        return res[k - 1]

    return -1


kthFactor(46, 4)