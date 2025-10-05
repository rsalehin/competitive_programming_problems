t = int(input().strip())
for _ in range(t):
    a, b, c = map(int, input().split())
    max_product = 0
    for da in range(6):
        for db in range(6 - da):
            dc = 5 - da - db
            product = (a + da) * (b + db) * (c + dc)
            max_product = max(max_product, product)
    print(max_product)
