from rich import print
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.prompt import Prompt
from rich.console import Console
from rich.console import Capture
import keyboard
import time


def main():
    console = Console()
    _width, _height = console.width, console.height
    console.size = (_width, _height-1)
    
    layout = Layout(size=console.height)
    layout.split_column(
        Layout(name="upper"),
        Layout(name="lower")
    )
    layout["upper"].update(
        Panel("[red]CLIRP")
    )
    layout["upper"].ratio = 1
    layout["lower"].ratio = 5

    

    while True:
        name = Prompt.ask("> ")
        layout["lower"].update(Panel(f"[blue]{name}"))
        console.log(layout)

                


main()