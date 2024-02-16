# try:
#     a = 18
#     b = 0    
#     c = a / b
# except ZeroDivisionError as e:
#     print(f'Error when dividing by zero {e}')
# except NameError as e:
#     print(f'Erro, variable not found {e}')
# except TypeError as e:
#     print(f'TypeError {e}')
# print('Fim')


def miniMaxSum(arr: []) -> str:
    # Write your code here
    max_number = max(arr)
    min_number = min(arr)
    
    max_number_index = arr.index(max_number)
    min_number_index = arr.index(min_number)
    
    print(max_number_index, min_number_index)

    print()

    arr_less_min = arr.pop(min_number_index)
    arr_less_max = arr.pop(max_number_index)
    
    max_sum = sum(arr_less_max)
    min_sum = sum(arr_less_min)
    
    print(f'{max_sum} {min_sum}')
    
    
if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
