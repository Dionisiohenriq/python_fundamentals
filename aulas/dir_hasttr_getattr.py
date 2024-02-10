string = 'Henrique'
method = 'sort'
# print(dir(string))

if hasattr(string, 'upper'):
    print('Exists upper')
    print(string.upper())

if getattr(string, 'lower'):
    print('Has lower')
    print(getattr(string, 'lower'))

if hasattr(string, method):
    print('Exists upper')
    print(getattr(string, method)())
else:
    print('Not exists this method', method)

