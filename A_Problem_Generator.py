t = int(input().strip())
for _ in range(t):
    questions, round = list(map(int, input().split()))
    bank = input().strip()
    freq = {'A':0,
            'B':0,
            'C':0,
            'D':0,
            'E' : 0,
            'F': 0, 
            'G': 0}
    for difficulty in bank:
        freq[difficulty]+= 1
    required = 0
    for key, value in freq.items():
        if freq[key] < round:
            required += round - value 
    print(required)