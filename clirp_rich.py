from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.prompt import Prompt
import time


def main():
    layout = Layout()
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].update(
        Panel("[red]CLIRP")
    )
    layout["upper"].ratio = 1
    layout["lower"].ratio = 5
    with Live(layout, refresh_per_second=4):
        for i in range(10):
            layout["lower"].update(Panel(f"[blue]{i}"))
            time.sleep(1)
            user_input = Prompt.ask("")
            layout["lower"].update(Panel(f"[green]{user_input}"))
            time.sleep(1)
main()