s = input("ФИО: ")
s = s.strip()
parts = s.split()
initials = ''.join(p[0] for p in parts)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(' '.join(parts))}")
