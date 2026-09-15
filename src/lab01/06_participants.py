N = int(input('in_1: '))

c = 0
for i in range(N):
    inp = input(f'in_{i + 2}: ').split()
    if inp[-1] == "True":
        c += 1
print(f'out: {c} {N - c}')
