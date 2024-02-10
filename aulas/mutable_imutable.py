list = []
dict = {}
set = set()
tuple = ()
string = ''
int = 0
float = 0.0
none = None
false = False
range = range(0)

def bool(value):
    return 'false' if not value else 'true'

print(f'{list=} {bool(list)}')
print(f'{dict=} {bool(dict)}')
print(f'{set=} {bool(set)}')
print(f'{tuple=} {bool(tuple)}')
print(f'{string=} {bool(string)}')
print(f'{int=} {bool(int)}')
print(f'{float=} {bool(float)}')
print(f'{none=} {bool(none)}')
print(f'{false=} {bool(false)}')
print(f'{range=} {bool(range)}')