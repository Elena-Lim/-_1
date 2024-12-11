today = []
tomorrow = []
other = []

HELP = '''
Список доступных команд:
* show - напечать все задачи
* todo - добавить задачу
* help - Напечатать help
'''

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == 'todo':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        if date == 'Сегодня': 
            today.append(task)
        elif date == 'Завтра':
            tomorrow.append(task)
        else:
            other.append(task)
        print(f'Задача {task} добавлена')
    elif command == 'show':
        print('Сегодня')
        print(today)      
        print('Завтра')
        print(tomorrow)
        print('Другие')
        print(other)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда!')
        print(HELP)  