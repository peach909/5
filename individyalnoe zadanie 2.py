Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
if __name__ == '__main__':
a = []
s = 0
p = 1
n = int(input())
for i in range(n):
element = float(input())
a.append(element)
a.sort(reverse=True)
for el in a:
p *= el
if el < 0:
s += el
print("Сумма отрицательных элементов списка = ", s)
print("Произведение элементов списка, расположенных между максимальным и минимальным элементами = ", p)
print("Отсортированный по возрастанию список: ", a)