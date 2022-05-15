Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import randint
cnt = 0
values = [randint(-50, 50) for _ in range(10)]
min_index = values.index(min(values))
max_index = values.index(max(values))
if max_index < min_index: min_index, max_index = max_index, min_index
for i in range(min_index+1,max_index):
   if values[i] > 0: cnt += 1
print(values)
print('Количество положительных значений между минимальным и максимальным значениями равно:', cnt)