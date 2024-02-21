
def summ_list(lst_main,lst_1,lst_2,lst_3):
    lst_main.extend(lst_1)
    lst_main.extend(lst_2)
    lst_main.extend(lst_3)

def check_task(lst):
    task = 0
    for i in lst:
        if i == 0:
            task += 1
    return task

main_company = [1,0,1,1,1,1,0,1,0,1,1,1,0,1]
first_company = [0,0,0]
second_company = [1,0,0,1,1]
third_company = [1,1,1,0,1]

summ_list(main_company,first_company,second_company,third_company)
print('Общий список задач:', main_company)
print('Количество невыполненных задач:', check_task(main_company))