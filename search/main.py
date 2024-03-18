import os

import click


@click.command()
@click.option("--path", type=str)
@click.option("--name")
def file_search(path, name):
    for (root, dirs, files) in os.walk(path):
        for f in files:
            print(f"files: {os.path.join(root, f)}")
        for d in dirs:
            print(f"dires: {os.path.join(root, d)}")
        print("----------------")



if __name__ == "__main__":
    file_search()
