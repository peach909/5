Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [float(i) for i in input().split()]
c = [1, 4, 5, 8, 9, 3]
for i in a:
    if i > 0:
        c.append(i)
n = c[0]
for i in range(1, len(c)):
    n -= c[i]
print(n)