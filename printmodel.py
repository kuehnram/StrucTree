from model import Entry

indentation = "│  "
folder = "├─"
folder_end = "└─"


def print_model(entry: Entry, depth: int = 0, is_last_folder: bool = False) -> None:
    if depth == 0:
        print(f"{indentation * depth}{entry.name}")
    else:
        if is_last_folder:
            print(f"{indentation * depth}{folder_end}{entry.name}")
        else:
            print(f"{indentation * depth}{folder}{entry.name}")
    for (i, child) in enumerate(entry.children):
        is_last_child = i + 1 == len(entry.children)
        print_model(child, depth + 1, is_last_child)
