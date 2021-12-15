from typing import List

from model import Entry

indentation = "  "
folder_pipe = "│"
folder = "├─"
folder_end = "└─"


def print_model(entry: Entry, depth: int = 0, is_last_folder: bool = False, print_pipes: List[bool] = [False]) -> None:
    """
    Prints the whole model starting from the given entry.
    :param entry: The root node from where to start printing
    :param depth: the current depths. Necessary to keep track of the indentation during recursion.
    :param is_last_folder: Whether this entry is the last folder in the list of siblings.
    :param print_pipes: List which keeps track about whether to draw a folder pipe or not. E.g. [False, True, True]
    means: No pipe at indentation 0, pipe at indentation 1 and pipe at indentation 2. Never draw pipes for indentation 0.
    :return:
    """

    if depth == 0:
        print(entry.name)
    else:
        line = ""

        # print indentation, only add indentation for places that are True in the print_pipes list
        for i in range(depth):
            if print_pipes[i]:
                line += folder_pipe
            else:
                line += " "
            line += indentation

        if is_last_folder:
            line += f"{folder_end}{entry.name}"
        else:
            line += f"{folder}{entry.name}"

        print(line)

    for (i, child) in enumerate(entry.children):
        is_last_child = i + 1 == len(entry.children)

        # if this child is the last child we should stop printing pipes for this position
        print_pipes_child = print_pipes.copy()
        print_pipes_child.append(not is_last_child)

        print_model(child, depth + 1, is_last_child, print_pipes_child)
