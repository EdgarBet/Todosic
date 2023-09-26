import time

from todomvc_tests.model import todos


def test_open():
    todos.maximize_window()
    todos.opened('First', 'Second', 'Third', 'Forth')
    time.sleep(3)
    todos.should('First', 'Second', 'Third', 'Forth')
    time.sleep(2)
    todos.edit('Third', 'Third++')
    time.sleep(2)
    todos.completed()
    time.sleep(2)
    todos.complete_solo('Third++')
    time.sleep(2)
    todos.clear_completed()
    time.sleep(2)
    todos.delete('Third++')
    time.sleep(2)
    todos.add_todos('First', 'Second')
    time.sleep(2)
    todos.should('First', 'Second')
    time.sleep(2)
    todos.edit('First', '1st')
    time.sleep(2)
    todos.delete('Second')
    time.sleep(2)
    todos.edit('1st', 'One')
    time.sleep(2)
    todos.should('One')
    time.sleep(2)
    todos.delete('One')
    time.sleep(2)
    todos.add_todos('Test_completed !!!!!')
    time.sleep(2)
    todos.should('Test_completed !!!!!')

