seq = ["ATATACGCGTA", "CTTCGGNGGA"]
print("Начинаем обработку последовательностей:")
for i, sequence in enumerate(seq):
    print(f"\nПоследовательность {i+1}: {sequence}")
    print(f"Длина: {len(sequence)} символов")
    print("Разбивка по нуклеотидам:")
    for j, nucleotide in enumerate(sequence):
        print(f"  Позиция {j+1}: {nucleotide}")
    print(f"\nПоследовательность {i+1} полностью обработана")
print("Цикл выполнен")