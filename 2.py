# Generator itaror
def try_generator(y):
    n = y
    n += 1
    print("bajarildi")
    yield n

    n *= 2
    print("bajarildi 2")
    yield n

    n += 10
    print("bajarildi 3")
    yield n

result = try_generator(3)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(result)