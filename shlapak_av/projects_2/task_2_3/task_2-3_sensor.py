name = input("Имя оператора")
result = input("Значение при0бора")
with open("C:/Users/Artem/Documents/shlapak_av/projects_2/task_2_3/sensor_log.txt", "a", encoding="utf-8") as sensor:
    sensor.write(f"{name}\t{result}")
print('Данные успешно сохранены в sensor_log.txt')