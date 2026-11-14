"""Task management screen."""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from nexora.theme import COLORS
from nexora.widgets.common import heading, action_button, text_field


class TasksScreen(BoxLayout):
    def __init__(self, database, **kwargs):
        super().__init__(orientation="vertical", padding=16, spacing=8, **kwargs)
        self.database = database
        self.title_input = text_field("What needs to get done?")
        self.add_widget(heading("Tasks"))
        self.add_widget(self.title_input)
        self.add_widget(action_button("Add task", self.add_task))
        self.items = BoxLayout(orientation="vertical", spacing=6)
        self.add_widget(self.items)
        self.refresh()

    def add_task(self):
        try:
            self.database.add_task(self.title_input.text)
            self.title_input.text = ""
            self.refresh()
        except ValueError:
            pass

    def refresh(self):
        self.items.clear_widgets()
        for task in self.database.list_tasks():
            status = "✓" if task["completed"] else "○"
            row = BoxLayout(size_hint_y=None, height="38dp")
            label = Label(text=f"{status}  {task['title']}", color=COLORS["text"], halign="left")
            label.bind(size=lambda widget, size: setattr(widget, "text_size", size))
            row.add_widget(label)
            if not task["completed"]:
                row.add_widget(action_button("Done", lambda task_id=task["id"]: self.complete(task_id)))
            row.add_widget(action_button("×", lambda task_id=task["id"]: self.remove(task_id),
                                         COLORS["danger"]))
            self.items.add_widget(row)

    def complete(self, task_id):
        self.database.set_task_completed(task_id)
        self.refresh()

    def remove(self, task_id):
        self.database.delete_task(task_id)
        self.refresh()
