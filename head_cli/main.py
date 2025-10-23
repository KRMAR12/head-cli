import click
import os
from colorama import init

init(autoreset=True)
def read_first_lines(file_path, num_lines=None, num_bytes=None):
    """Reads the first lines or bytes from the beginning of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    if num_bytes: 
        with open(file_path, 'rb') as f:
            data = f.read(num_bytes)
        return data.splitlines()

    elif num_lines:  
        lines = []
        with open(file_path, 'rb') as f:
            for _ in range(num_lines):
                line = f.readline()
                if not line:
                    break
                lines.append(line.rstrip(b'\n'))
        return lines

    else:
        raise ValueError("Specify num_lines or num_bytes.")


@click.command(help="Prints the first N lines or bytes of a file (from the start).")
@click.argument("file", type=click.Path(exists=True))
@click.option("-n", "--lines", type=int, default=None, help="Number of lines to output (from start)")
@click.option("-c", "--bytes", "num_bytes", type=int, default=None, help="Number of bytes to output (from start)")
@click.option("-u", "--uppercase", is_flag=True, help="Display text in uppercase letters")
@click.option("--reverse", is_flag=True, help="Display lines in reverse order")
@click.option("--number", is_flag=True, help="Add line numbering")
@click.option("--color", is_flag=True, help="Color output (yellow)")
def main(file, lines, num_bytes, uppercase, reverse, number, color):
    try:
        raw_lines = read_first_lines(file, num_lines=lines, num_bytes=num_bytes)
        text_lines = [l.decode('utf-8', errors='ignore') for l in raw_lines]

        for i, line in enumerate(text_lines, 1):
            output = line
            if number:
                output = f"{i}\t{output}"
            if uppercase:
                output = output.upper()
            if reverse:
                output = output[::-1]
            if color:
                output = click.style(output, fg="yellow")
            click.echo(output)

    except FileNotFoundError:
        click.echo(f"File '{file}' not found.", err=True)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    main()
