import random

def monte_carlo_area(n):
    inside = 0

    for _ in range(n):
        x = random.uniform(4, 8)
        y = random.uniform(2, 5)

        if 5 <= x <= 7 and 3 <= y <= 4:
            inside += 1

    area_big = (8 - 4) * (5 - 2)
    area = (inside / n) * area_big
    return area

exact_area = 2

n_values = [100, 500, 1000, 5000, 10000, 50000, 100000]

print("N | Приближенная площадь | Ошибка")

for n in n_values:
    result = monte_carlo_area(n)
    error = abs(exact_area - result)
    print(n, "|", result, "|", error)