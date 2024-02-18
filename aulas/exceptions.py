try:
    a = 18
    b = 0    
    c = a / b
except ZeroDivisionError as e:
    print(f'Error when dividing by zero {e}')
except NameError as e:
    print(f'Erro, variable not found {e}')
except (TypeError, IndexError) as e:
    print(f'TypeError {e}')
except Exception as e:
    print(f'Error {e}')
print('Fim')


# def miniMaxSum(arr: []) -> str:
#     # Write your code here
#     arr2 = arr.copy()
    
#     arr.remove(max(arr))
#     arr2.remove(min(arr))
    
#     max_sum = sum(arr)
#     min_sum = (sum(arr2))

#     print(f'{max_sum} {min_sum}')
    

# if __name__ == '__main__':

#     arr = [1, 2, 3, 4, 5]

#     miniMaxSum(arr)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# def gradingStudents(grades):
    # Write your code here
    # count_difference = 0
    # index = 0
    # grade_aux = 0
    
    # print(grades)
    
    # for grade in grades:
        
    #     print(grade)

    #     grade_aux = grade
        
    #     if grade > 37:
                
    #         while grade_aux % 5 != 0:
    #             count_difference += 1
    #             grade_aux += 1
            
    #         if count_difference < 3:
    #             print(grade, grade_aux)
    #             grade = grade_aux
    #             grades[index] = grade
        
    #     index += 1
    #     count_difference = 0
        
    # return grades
#     return map(lambda grade: round(grade * 2, -1) // 2 if grade >= 38 and grade % 5 >= 3 else grade, grades)

# if __name__ == '__main__':

#     grades = [73, 67, 38, 33]

#     result = gradingStudents(grades)

#     print(result)
