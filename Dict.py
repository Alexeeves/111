# Программа берет словарь и меняет местами ключи и значения.

a = {'name': 'ivan', 'surname': 'ivanov'}
b = {v: k for k, v in a.items()}
print(b)
