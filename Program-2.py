def generate_odd_series(x):
    result = []
    for i in range(x):
        result.append(2 * i + 1)
    print(", ".join(map(str, result)))


generate_odd_series(4) 
