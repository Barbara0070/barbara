x = 0
while x < 101:
    if x % 10 == 0:
        x += 1
        continue
    print("x: ", x, "x^2: ", x ** 2)
    x = x + 1
