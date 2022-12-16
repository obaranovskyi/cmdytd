from rich import print

blue = "turquoise2"
red = "deep_pink2"
green = "spring_green1"
yellow = "yellow"

def info(message):
    print(f"[{blue}]{message}")

def error(message):
    print(f"[{red}]{message}")

def help_details(command_name, description):
    print(f"[{blue}]  {command_name}[{green}] - {description}")


def print_download_progress(vid, _, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    total_size = (total_size/1024)/1024
    total_size = round(total_size, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    downloaded = (bytes_downloaded / 1024) / 1024
    downloaded = round(downloaded, 1)
    percentage_of_completion = round(percentage_of_completion, 2)

    print(f'[{blue}]Download Progress: [{yellow}]{percentage_of_completion}% | ' +
          f'[{blue}]Total Size: [{yellow}]{total_size}MB | ' +
          f'[{green}]Downloaded: [{yellow}]{downloaded}MB | ' +
          f'[{red}]Remaining: [{yellow}]{remain}MB  ', end='\r')
