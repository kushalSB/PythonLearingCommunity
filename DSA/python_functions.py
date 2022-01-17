def my_fxn(value):

    if (value == 1):
        return 1
    else:
        return value * my_fxn(value-1)

print(my_fxn(5))