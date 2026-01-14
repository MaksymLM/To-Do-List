menu = ["1. Добавить задачу 2. Посмотреть задачи 3. Удалить задачу 4. Выйти"]
choise = []
tasks = []

def add_task():
    while True:
        task = input("Write a task: ")
        if task == "stop":
            return
        tasks.append(task)

def remove_task():
    while True:
        task = input("Write a task: ")
        if task == "stop":
            return
        tasks.remove(task)

def show_tasks():
    while True:
        print(tasks)
        return

while True:
    print(menu)
    choise = input("Choose a function: ")
    if choise == "1":
        add_task()

    elif choise == "2":
        remove_task()

    elif choise == "3":
        show_tasks()

    elif choise == "4":
        break



# мейби не пригодится
function = []
print("My functions are:")
print("Add new goal, delete a goal, show To-do-List")
function = input("Choose a function: ")

goals = []

while True:
    if goals == "exit":
        function = input("Choose a function: ")

    if goals == "close":
        break

    if function == "Add new goal":
        goals = input("Add your new goal: ")

    if function == "delete a goal":
        goals.remove(input("Write a goal: "))

    if function == "show To-do-List":
        print(goals)

menu = ["1. Добавить задачу 2. Посмотреть задачи 3. Удалить задачу 4. Выйти"]
choise = []
tasks = []

while True:
    print(menu)
    choice = input("Choose a function: ")

    if choice == "1":
        tasks.append(input("Write a task: "))



