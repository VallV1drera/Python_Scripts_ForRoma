import time
import typer
from rich.progress import track

def main():
    total = 0
    for value in track(range(100), description="Processing..."):
        time.sleep(1)
        total += 1
    input()

if __name__ == "__main__":

    typer.run(main)
