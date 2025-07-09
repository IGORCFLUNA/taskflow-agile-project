from src import main

def test_create_task():
    main.create_task("Testar", "Alta")
    assert main.tasks[-1]["title"] == "Testar"
    assert main.tasks[-1]["priority"] == "Alta"