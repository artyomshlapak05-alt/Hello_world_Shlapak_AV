files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = "26.02.2026"  
print("Обработка файлов:")
for name in files:
    new_name = f"{name}_{sample_date}.fasta"
    print(f"Исходный файл: {name:8} -> Новый файл: {new_name}")
print(f"Все файлы обработаны с датой: {sample_date}")