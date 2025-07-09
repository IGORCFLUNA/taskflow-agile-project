tasks = []

def create_task(title, priority):
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False
    })

def list_tasks():
    for task in tasks:
        print(task)

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True

if __name__ == "__main__":
    create_task("Revisar backlog", "Alta")
    create_task("Deploy inicial", "Média")
    list_tasks()