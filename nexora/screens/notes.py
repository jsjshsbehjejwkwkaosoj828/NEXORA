"""Quick notes screen."""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from nexora.theme import COLORS
from nexora.widgets.common import heading, action_button, text_field


class NotesScreen(BoxLayout):
    def __init__(self, database, **kwargs):
        super().__init__(orientation="vertical", padding=16, spacing=8, **kwargs)
        self.database = database
        self.title_input = text_field("Note title")
        self.body_input = text_field("Write something worth keeping…", multiline=True)
        self.add_widget(heading("Notes"))
        self.add_widget(self.title_input)
        self.add_widget(self.body_input)
        self.add_widget(action_button("Save note", self.save_note))
        self.items = BoxLayout(orientation="vertical", spacing=6)
        self.add_widget(self.items)
        self.refresh()

    def save_note(self):
        try:
            self.database.add_note(self.title_input.text, self.body_input.text)
            self.title_input.text = ""
            self.body_input.text = ""
            self.refresh()
        except ValueError:
            pass

    def refresh(self):
        self.items.clear_widgets()
        for note in self.database.list_notes():
            row = BoxLayout(size_hint_y=None, height="44dp")
            row.add_widget(Label(text=f"{note['title']} — {note['body']}",
                                 color=COLORS["text"], halign="left"))
            row.add_widget(action_button("×", lambda note_id=note["id"]: self.remove(note_id),
                                         COLORS["danger"]))
            self.items.add_widget(row)

    def remove(self, note_id):
        self.database.delete_note(note_id)
        self.refresh()
