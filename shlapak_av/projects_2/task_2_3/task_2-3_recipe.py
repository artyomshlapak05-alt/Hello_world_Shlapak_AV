environment = input('Название среды:')
agar_percentage = input('Процентное содержание агара:')
ster_temperature = input('Температура стерилизации:')
environment_up = environment.upper
with open('recipe.txt', 'w', encoding='utf-8') as recipe:
    recipe.write(f'{environment_up}\nПроцентное содержание агара\t{agar_percentage}\nТемпература стерилизации\t{ster_temperature}')