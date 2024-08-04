try:
    print('open file')
    print(8/0)
except ZeroDivisionError:
    raise ValueError("Error")
finally:
    print('fim')