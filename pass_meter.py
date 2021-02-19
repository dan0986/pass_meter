"""Password meter module"""

import urwid
from pass_calculator import calculate_password_strength


def main():
    """Main entry script."""

    def on_ask_change(value, new_value):
        reply.set_text(
            "Рейтинг пароля: {}".format(calculate_password_strength(new_value))
        )

    ask = urwid.Edit("Введите пароль: ")
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign="middle")
    urwid.connect_signal(ask, "change", on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
