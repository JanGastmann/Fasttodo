class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Aufgabe "{task}" hinzugefügt.')

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f'Aufgabe "{task}" entfernt.')
        except ValueError:
            print(f'Aufgabe "{task}" nicht gefunden.')

    def show_tasks(self):
        if not self.tasks:
            print('Die To-Do-Liste ist leer.')
        else:
            print('To-Do-Liste:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Aufgabe hinzufügen')
        print('2. Aufgabe entfernen')
        print('3. To-Do-Liste anzeigen')
        print('4. Beenden')

        choice = input('Bitte wählen Sie eine Option (1/2/3/4): ')

        if choice == '1':
            task = input('Geben Sie die Aufgabe ein: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Geben Sie die Aufgabe ein, die Sie entfernen möchten: ')
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print('Programm wird beendet.')
            break
        else:
            print('Ungültige Eingabe. Bitte wählen Sie 1, 2, 3 oder 4.')

if __name__ == "__main__":
    main()
