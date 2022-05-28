import time
import click


def start_countdown(duration, minimal):
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = f"{mins:02}:{secs:02}"
        output = f"{timeformat}\r" if minimal else f"🍅 Time remaining - {timeformat}\r"
        click.echo(output, nl=False)
        time.sleep(1)
        duration -= 1

    print("Timer ended.")


@click.command()
@click.option("-d", "--duration", default=25, show_default=True, help="The timer duration in minutes")
@click.option("-s", "--in-seconds", is_flag=True, default=False, show_default=True, help="Timer duration is provided in seconds")
@click.option("-m", "--minimal", is_flag=True, default=False, show_default=True, help="Print minimal timer output")
def cli(duration, in_seconds, minimal):
    """Starts a pomodoro timer countdown."""
    duration_in_seconds = duration if in_seconds else duration * 60

    start_countdown(duration_in_seconds, minimal)
