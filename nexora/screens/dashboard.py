"""Dashboard screen."""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from nexora.theme import COLORS
from nexora.widgets.common import heading


class DashboardScreen(BoxLayout):
    def __init__(self, database, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=12, **kwargs)
        self.database = database
        self.add_widget(heading("Your overview"))
        self.metrics = Label(color=COLORS["text"], halign="left", valign="top")
        self.metrics.bind(size=lambda widget, size: setattr(widget, "text_size", size))
        self.add_widget(self.metrics)
        self.refresh()

    def refresh(self):
        data = self.database.summary()
        self.metrics.text = (
            f"Tasks created       {data['tasks_total']}\n"
            f"Tasks completed     {data['tasks_completed']}\n"
            f"Focus sessions      {data['focus_sessions']}\n"
            f"Focused time        {data['focus_minutes']} min\n\n"
            "Small, consistent steps add up."
        )
