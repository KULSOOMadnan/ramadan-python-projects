import click
import json
import os

TODO_FILE = "todo.json"

def todo_task():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    # If file doesn't exist, create it with empty list
    with open(TODO_FILE, "w") as file:
        json.dump([], file)
    return []
            
def save_todo(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """Simple CLI for managing your todo list"""
    pass

@cli.command()
@click.argument("task")
def add(task):
    """Add a new task to the todo list"""
    todos = todo_task()
    todos.append({"task": task, "completed": False})
    save_todo(todos)
    click.echo(f"Task '{task}' added to the todo list.")
    
@cli.command()
def list():
    """List all the tasks in the todo list"""
    todos = todo_task()
    if not todos:
        click.echo("No tasks in the todo list.")
        return
    for index, todo in enumerate(todos, start=1):
        status = '✅' if todo['completed'] else '❌'
        click.echo(f"{index}.  {todo['task']} {status}")
        
@cli.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as Completed"""
    tasks = todo_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_todo(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number. Please try again.")
        
@cli.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the todo list"""
    tasks = todo_task()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_todo(tasks)
        click.echo(f"Succesfully Removed task: {removed_task['task']} from the todo list")
    else:
        click.echo(f"Invalid task number. Please try again.")

if __name__ == "__main__":
    cli()
