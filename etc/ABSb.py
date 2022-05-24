def sum_total():
    n, a, b = map(int, raw_input().split())
    l = []

    for i in range(1,n+1):
        n_sum = sum(list(map(int,str(i))))
        if a <= n_sum and n_sum <= b:
            l.append(i)

    l_sum = sum(l)
    print(l_sum)
sum_total()
