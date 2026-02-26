total = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input("Введите вместимость одной упаковки: "))
packs = total // capacity
remaining = total % capacity
print(f"\nПолных упаковок: {packs}")
print(f"Останется капсул: {remaining}")