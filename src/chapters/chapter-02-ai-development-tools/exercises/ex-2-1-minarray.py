def minarray(xl):
    m = xl[0]
    for x in xl:
        if x < m:
            m = x
    return m


data = [12, 3, 4, 5, 6, 7, 8, 9, 10]
t = minarray(data)
print(t)