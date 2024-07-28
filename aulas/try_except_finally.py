try:
    print('open file')
except ZeroDivisionError:
    raise("Error")
finally:
    print('fim')