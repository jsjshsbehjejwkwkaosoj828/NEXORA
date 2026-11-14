"""Reusable Kivy widgets."""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from nexora.theme import COLORS


def heading(text: str) -> Label:
    return Label(text=text, color=COLORS["text"], bold=True, font_size="22sp",
                 size_hint_y=None, height="48dp", halign="left")


def action_button(text: str, callback, color=None) -> Button:
    button = Button(text=text, size_hint_y=None, height="44dp",
                    background_normal="", background_color=color or COLORS["primary"],
                    color=COLORS["text"])
    button.bind(on_release=lambda *_: callback())
    return button


def text_field(hint: str, multiline: bool = False) -> TextInput:
    return TextInput(hint_text=hint, multiline=multiline, size_hint_y=None,
                     height="44dp" if not multiline else "100dp",
                     background_normal="", background_active="",
                     background_color=COLORS["surface_alt"],
                     foreground_color=COLORS["text"],
                     hint_text_color=COLORS["muted"], padding=12)
