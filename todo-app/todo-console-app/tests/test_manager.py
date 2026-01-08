import pytest
from todo_app.manager import TaskManager

def test_add_task_valid():
    """Test adding a task with valid title and description."""
    manager = TaskManager()
    task_id = manager.add_task("Buy milk", "At the corner store")
    
    assert task_id == 1
    task = manager.get_task(task_id)
    assert task is not None
    assert task.title == "Buy milk"
    assert task.description == "At the corner store"
    assert task.status is False

def test_add_task_empty_title():
    """Test that adding a task with an empty title raises ValueError."""
    manager = TaskManager()
    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.add_task("")

def test_add_task_whitespace_title():
    """Test that adding a task with only whitespace raises ValueError."""
    manager = TaskManager()
    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.add_task("   ")

def test_id_auto_increment():
    """Test that task IDs auto-increment and are never reused."""
    manager = TaskManager()
    id1 = manager.add_task("Task 1")
    id2 = manager.add_task("Task 2")
    
    assert id1 == 1
    assert id2 == 2
    assert len(manager.get_all_tasks()) == 2

def test_get_task_not_found():
    """Test retrieving a task that doesn't exist."""
    manager = TaskManager()
    assert manager.get_task(999) is None

def test_get_all_tasks_empty():
    """Test retrieving all tasks when list is empty."""
    manager = TaskManager()
    assert manager.get_all_tasks() == []

def test_update_task_success():
    """Test updating task details."""
    manager = TaskManager()
    task_id = manager.add_task("Old Title", "Old Desc")
    
    assert manager.update_task(task_id, title="New Title", description="New Desc") is True
    task = manager.get_task(task_id)
    assert task.title == "New Title"
    assert task.description == "New Desc"

def test_update_task_partial():
    """Test updating only one field."""
    manager = TaskManager()
    task_id = manager.add_task("Title", "Desc")
    
    manager.update_task(task_id, title="Updated Title")
    task = manager.get_task(task_id)
    assert task.title == "Updated Title"
    assert task.description == "Desc"
    
    manager.update_task(task_id, description="Updated Desc")
    assert task.description == "Updated Desc"

def test_update_task_not_found():
    """Test updating a non-existent task."""
    manager = TaskManager()
    assert manager.update_task(999, title="Whatever") is False

def test_update_task_invalid_title():
    """Test that updating to an empty title raises ValueError."""
    manager = TaskManager()
    task_id = manager.add_task("Title")
    with pytest.raises(ValueError, match="Title cannot be empty"):
        manager.update_task(task_id, title="")

def test_toggle_task_status():
    """Test toggling task status."""
    manager = TaskManager()
    task_id = manager.add_task("Test Toggle")
    
    assert manager.get_task(task_id).status is False
    assert manager.toggle_task_status(task_id) is True
    assert manager.get_task(task_id).status is True
    
    assert manager.toggle_task_status(task_id) is True
    assert manager.get_task(task_id).status is False

def test_toggle_task_not_found():
    """Test toggling a non-existent task."""
    manager = TaskManager()
    assert manager.toggle_task_status(999) is False

def test_delete_task_success():
    """Test deleting a task."""
    manager = TaskManager()
    task_id = manager.add_task("To Be Deleted")
    
    assert len(manager.get_all_tasks()) == 1
    assert manager.delete_task(task_id) is True
    assert len(manager.get_all_tasks()) == 0
    assert manager.get_task(task_id) is None

def test_delete_task_not_found():
    """Test deleting a non-existent task."""
    manager = TaskManager()
    assert manager.delete_task(999) is False



