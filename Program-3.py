def generate_conditional_odd_series(x):
    result = []
    for i in range(1, x + 1):
        if i % 2 != 0:
            result.append(2 * len(result) + 1)
    print(", ".join(map(str, result)))


generate_conditional_odd_series(6) 
