from rich import print
from rich.panel import Panel
from rich.layout import Layout

def main():
    # print(Panel("[Blue]Welcome to Clirp: A RPN calculator for your terminal!"))
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
    print(layout)
main()