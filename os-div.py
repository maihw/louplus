import os

def view_dir(path='.'):
    """
    this is a def:print all file in the div
    :args pth:the div
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end ="")
    print()
