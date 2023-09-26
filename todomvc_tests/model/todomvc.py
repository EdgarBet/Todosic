from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

completed = have.css_class('completed')


class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open_browser(self):
        browser.open('https://todomvc.com/examples/emberjs/')
        # app_loaded = "return $._data('#clear-completed')[0], 'events')" \
        #              ".hasOwnProperty('click')"
        # browser.should(have.js_returned(True, app_loaded))
        return self

    def maximize_window(self):
        browser.driver.maximize_window()
        return self

    def add_todos(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def opened(self, *todos: str):
        self.open_browser()
        self.add_todos(*todos)

    def should(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return self.todo_list.element_by(have.css_class('editing')).element('.edit').perform(
            command.js.set_value(new_text))

    def edit(self, todo, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def complete_solo(self, task):
        self.todo_list.element_by(have.exact_text(task)).element('.toggle').click()
        return self

    def completed(self):
        s("#toggle-all").click()
        return self

    def clear_completed(self):
        s("#clear-completed").click()
        return self

    def delete(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)) \
            .hover().element('.destroy').click()
        return self


