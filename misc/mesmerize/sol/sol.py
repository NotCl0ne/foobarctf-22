"""
It is an implementation of Hilbert curve, 
but you can find a mapping easily and reverse chall.txt to flag.txt
"""
from math import isqrt

def rotate(point: list[int], rx: int, ry: int, n: int) -> None:
    if ry != 0:
        return
    if rx == 1:
        point[0] = n - 1 - point[0]
        point[1] = n - 1 - point[1]
    point[0] = point[0] + point[1]
    point[1] = point[0] - point[1]
    point[0] = point[0] - point[1]


def index_to_point(index: int, order: int) -> list[int]:
    n = pow(2, order)
    point = [0, 0]
    s = 1
    t = index
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        rotate(point, rx, ry, s)
        point[0] += s * rx
        point[1] += s * ry
        t //= 4
        s *= 2
    return point

if __name__ == '__main__':
    with open('chall.txt') as file:
        mesmerized = [c.strip() for c in file.readlines()]
    order = isqrt(len(mesmerized) * len(mesmerized[0]))
    row = 32
    chars = [
        [ [''] for _ in range(order) ] for _ in range(order)
    ]
    for i in range(pow(order, 2)):
        x, y = index_to_point(i, order)
        chars[y][x] = mesmerized[i % row][i // row]
    with open('flag.txt', 'w') as file:
        file.writelines([
            ''.join(c) + '\n' for c in chars
        ])
