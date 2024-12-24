def for_gen(start, stop):
    for i in range(start, stop):
        yield i
result = for_gen(1, 5)
print(result)

for item in result:
    print(item)
def generator(a, b):
    s = 0
    for i in range(a, b, -1):
        s += i
        yield s
r = generator(20,10)
for item in r:
    print(item)
# Anonim generator
anonim =  [a for a in range(1000)]
print(anonim)

my_generator = (b for b in range(15))
print(my_generator)
for i in my_generator:
    print(i)
