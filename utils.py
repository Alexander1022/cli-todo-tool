import os
import datetime

TODO_FILE = 'data/todo.txt'

# checks if there is a data folder and a logs folder inside it
# if not, it creates them
def dir_check():
    if not os.path.exists('data'):
        if not os.path.exists('data/logs'):
            os.makedirs('data/logs')

def create_todo_file():
    if not os.path.exists('data/logs/todo.txt'):
        open('data/todo.txt', 'w').close()


def today_date():
    today = datetime.date.today()
    return today.strftime("%d-%m-%Y")