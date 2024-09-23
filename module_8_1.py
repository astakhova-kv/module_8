def add_everything_up(a, b):
    try:
        return (round(a + b, 10))
    except(TypeError):
        if isinstance(a, int) or isinstance(a, float):
            a = str(a)
        if isinstance(b, int) or isinstance(b, float):
            b = str(b)
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
