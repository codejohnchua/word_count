import click
import sys

@click.command()
@click.option('-c', is_flag=True, show_default=True, default=False, help='Count bytes in file')
@click.option('-l', is_flag=True, show_default=True, default=False, help='Count lines in file')
@click.option('-w', is_flag=True, show_default=True, default=False, help='Count words in file')
@click.argument('file', type=click.File('r', encoding='utf8'), default=sys.stdin)
def ccwp(c: bool, l: bool, w: bool, file: click.File) -> None:
    if file == None:
        click.echo("No file")
        return

    file_str = file.read()
    
    output = ""
    if c:
        output += str(count_bytes(file_str))
    elif l:
        output += str(count_lines(file_str))
    elif w:
        output += str(count_words(file_str))
    else:
        output += str(count_lines(file_str)) + " "
        output += str(count_words(file_str)) + " "
        output += str(count_bytes(file_str))
    output += " " + file.name
    click.echo(output)

def count_bytes(file_str: str) -> int:
    file_bytes = bytes(file_str, 'utf8')
    return len(file_bytes)

def count_lines(file_str: str) -> int:
    return len(file_str.split('\n')) - 1

def count_words(file_str: str) -> int:
    return len(file_str.split())

if __name__ == '__main__':
    ccwp()