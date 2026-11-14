"""NEXORA Kivy application composition."""
from pathlib import Path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from nexora.database import Database
from nexora.screens.dashboard import DashboardScreen
from nexora.screens.tasks import TasksScreen
from nexora.screens.notes import NotesScreen
from nexora.screens.focus import FocusScreen
from nexora.theme import COLORS


class NexoraApp(App):
    title = "NEXORA"

    def build(self):
        data_dir = Path(self.user_data_dir)
        data_dir.mkdir(parents=True, exist_ok=True)
        self.database = Database(data_dir / "nexora.sqlite3")

        root = BoxLayout(orientation="vertical", spacing=8, padding=10)
        root.canvas.before.clear()
        from kivy.graphics import Color, Rectangle
        with root.canvas.before:
            Color(*COLORS["background"])
            self.background = Rectangle(pos=root.pos, size=root.size)
        root.bind(pos=self._sync_background, size=self._sync_background)

        header = Label(text="◈  N E X O R A", size_hint_y=None, height="54dp",
                       color=COLORS["text"], bold=True, font_size="22sp")
        root.add_widget(header)

        manager = ScreenManager(transition=FadeTransition())
        screens = {
            "home": DashboardScreen(self.database),
            "tasks": TasksScreen(self.database),
            "notes": NotesScreen(self.database),
            "focus": FocusScreen(self.database),
        }
        for name, widget in screens.items():
            screen = Screen(name=name)
            screen.add_widget(widget)
            manager.add_widget(screen)
        root.add_widget(manager)

        nav = BoxLayout(size_hint_y=None, height="48dp", spacing=5)
        for name, label in [("home", "Home"), ("tasks", "Tasks"),
                            ("notes", "Notes"), ("focus", "Focus")]:
            button = Button(text=label, background_normal="",
                            background_color=COLORS["surface_alt"],
                            color=COLORS["text"])
            button.bind(on_release=lambda _btn, target=name: setattr(manager, "current", target))
            nav.add_widget(button)
        root.add_widget(nav)
        self.screen_manager = manager
        return root

    def _sync_background(self, widget, _value):
        self.background.pos = widget.pos
        self.background.size = widget.size

    def on_stop(self):
        pass
