s = input('in: ')
out = ''
start_i = 0
step = 0

for i in range(len(s)):
    if s[i].isupper():
        start_i = i
        while not s[i + step].isnumeric():
            step += 1
        step += 1
        break

for i in range(start_i, len(s), step):
    out += s[i]

print(f'out: {out}')