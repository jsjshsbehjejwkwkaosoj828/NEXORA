"""Focus timer screen."""
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from nexora.theme import COLORS
from nexora.widgets.common import heading, action_button, text_field


class FocusScreen(BoxLayout):
    def __init__(self, database, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=12, **kwargs)
        self.database = database
        self.remaining = 25 * 60
        self.event = None
        self.add_widget(heading("Focus"))
        self.duration = text_field("Session length in minutes (default 25)")
        self.add_widget(self.duration)
        self.clock_label = Label(text="25:00", color=COLORS["accent"], font_size="48sp")
        self.add_widget(self.clock_label)
        self.add_widget(action_button("Start / restart", self.start))
        self.add_widget(action_button("Pause", self.pause))
        self.add_widget(action_button("Reset", self.reset))

    def start(self):
        self.pause()
        try:
            minutes = int(self.duration.text) if self.duration.text.strip() else 25
            if not 5 <= minutes <= 120:
                raise ValueError
        except ValueError:
            self.clock_label.text = "Choose 5–120 min"
            return
        self.remaining = minutes * 60
        self.clock_label.text = self.format_time()
        self.event = Clock.schedule_interval(self.tick, 1)

    def tick(self, _dt):
        self.remaining -= 1
        self.clock_label.text = self.format_time()
        if self.remaining <= 0:
            self.pause()
            minutes = max(1, int(self.duration.text or 25))
            self.database.log_focus_session(minutes)
            self.clock_label.text = "Session complete!"
            return False
        return True

    def pause(self):
        if self.event:
            self.event.cancel()
            self.event = None

    def reset(self):
        self.pause()
        self.remaining = 25 * 60
        self.clock_label.text = self.format_time()

    def format_time(self):
        return f"{self.remaining // 60:02d}:{self.remaining % 60:02d}"
