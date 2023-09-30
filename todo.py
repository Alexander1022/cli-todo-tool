import click 
import os 

# define the file path for storing the todo list 

TODO_FILE = "todo.txt"

if not os.path.exists(TODO_FILE):
    open(TODO_FILE, "w").close()

@click.group()
def cli():
    pass 

@cli.command()
@click.argument("task")
def add (task):
    """Add a new task to the todo list"""
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
        click.echo(f'Task "{task}" added to the todo list.')

# error here i cant see the tasks with python todo.py list
@cli.command()
def list ():
    """List all tasks in the to do list."""
    if os.path.getsize(TODO_FILE) == 0:
        click.echo("No tasks in the todo list")
    else:
        with open(TODO_FILE, "r") as file:
            tasks = file.read().splitlines
            click.echo("Todo list: ")
            for i, task in enumerate(tasks, start=1):
                click.echo(f"{i}.{task}")

@cli.command()
@click.argument("task_numbe", type=int)
def remove(task_number):
    """Remove a task from the todo list by its number"""
    with open(TODO_FILE, 'r') as file:
        tasks = file.read().splitlines()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(TODO_FILE, 'w') as file:
            file.write('\n'.join(tasks))
        click.echo(f'Task "{removed_task}" removed from the todo list.')
    else:
        click.echo('Invalid task number.')
    
    #
if __name__ == '__main__':
    cli()