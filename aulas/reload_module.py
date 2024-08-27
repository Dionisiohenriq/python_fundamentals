import importlib
import python_modules


print(123)

for i in range(10):
    print(i)
    importlib.reload(python_modules)

