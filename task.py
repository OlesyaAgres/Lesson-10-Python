# Урок 10. Построение графиков
# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


#  Решение

def print_operation_table(operation, num_rows, num_сolumns):
    arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns+1)]
    for i in arr:
        print(*[f"{x:>3}"for x in i])
line = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda x,y: x*y,line,columns)