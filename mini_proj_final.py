import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

task_list = {'running': 'incomplete', 'bathing': 'incomplete'}

def new_task(): #must add a new task and by default have it as incomplete
    while True:
        task = input("Enter task you'd like to add OR enter 'back' to return to menu: ").lower().strip()
        if task == 'back':
            break
        else:
            task_list[task] = 'incomplete'  #defaults every new entry to incomplete
        print() #cosmetic
        print('Your current list:')  #shows user an updated list every time they add
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for key, value in task_list.items():    #prints both 'key' and ''value' in dictionary
            print(Style.BRIGHT + key.title())
            print(Style.DIM + Fore.LIGHTRED_EX + value.title())
        print()

def view_task():    #should let you see the task list
    if task_list:
        print('Your current list:')  #shows user an updated list every time they add
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        for key, value in task_list.items():
            print(Style.BRIGHT + key.title())
            if value == 'incomplete':
                print(Style.DIM + Fore.LIGHTRED_EX + value.title())
            else:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + value.title())
    else:
        print("You have no tasks!")

def comp_task():  #should let you change a task from the default incomplete to complete
    while True:
        while True:
            show_list = input('Would you like to see a list of your current tasks?(y/n) ').lower().strip()
            if show_list == 'y':
                for key, value in task_list.items():
                    print(Style.BRIGHT + key.title())   #title case makes for good presentation
                    if value == 'incomplete':
                        print(Style.DIM + Fore.LIGHTRED_EX + value.title())
                    else:
                        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + value.title())
                print()
                break    
            elif show_list == 'n':
                break   
            else:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "            Please enter either 'y' or 'n'")
        try:
            update = input('Which task would you like to mark as complete? ').lower().rstrip()
            print()
            if update not in task_list:
                raise KeyError(f"{update} is not a task on you list")
            task_list[update] = 'complete'
            print(Fore.GREEN + f'      {update.title()} has been updated to {Style.BRIGHT + task_list[update]}\n') 
            break
        except KeyError as grace:
            print('               ', Fore.RED + Style.BRIGHT + str(grace) + Fore.RESET, '\n') 
            print(Fore.LIGHTRED_EX + '                      Please, try again\n')
    return task_list    

            
def del_task(): #should let you delete task
    while True:
        while True:
            show_list = input('Would you like to see a list of your current tasks?(y/n) ').lower().strip() #'lower' and 'strip' help facilitate user entry
            print()
            if show_list == 'y':
                print('Your current list:')  #shows user an updated list every time they add
                print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
                for key, value in task_list.items():
                    print(Style.BRIGHT + key.title())
                    if value == 'incomplete':
                        print(Style.DIM + Fore.LIGHTRED_EX + value.title())
                    else:
                        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + value.title())
                print()
                break  
            elif show_list == 'n':
                break
            else:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "            Please enter either 'y' or 'n'")
        if task_list:
            task = input("Enter task you'd like to remove OR enter 'back' to return to menu: ").lower().rstrip()
            print()
            if task == 'back':
                break
            elif task in task_list.keys():
                del task_list[task]
                print(Style.BRIGHT + task.title(), 'has been', Style.BRIGHT + Fore.RED + 'deleted','\n')
            else:
                print('            ',task, Fore.LIGHTYELLOW_EX + Style.BRIGHT + "is not in your list")
        else:
            print('         _____________________________')
            print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '          Theres nothing in your list')
            print('         ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
            break
        


def main_application():
    while True:
        print()
        print(Style.BRIGHT + '             Welcome to TaskTracker!\n')

        print(Fore.LIGHTWHITE_EX +'                      Menu:')
        print(Fore.LIGHTWHITE_EX + Style.BRIGHT +'           --------------------------')
        print(Fore.RED +'''    
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit\n''')

        user_sel = input('''      What would you like to accomplish today?
                Enter 1,2,3,4 or 5
                     --> ''').strip()
        print()
        if user_sel == '1':
            new_task()
        elif user_sel == '2':
            view_task()
        elif user_sel == '3':
            comp_task()
        elif user_sel == '4':
            del_task()
        elif user_sel == '5':   #Dont need a sep func for this since all I need it to do is break.
            print('          ', Fore.LIGHTYELLOW_EX + 'Thanks for using TaskTracker')
            print('              ', Back.LIGHTYELLOW_EX + Style.BRIGHT +' We miss you already! ')
            print()
            break
        else:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '         Please enter a valid menu option')
        

main_application()