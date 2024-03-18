import  click
import glob

@click.command()
@click.option("--path", 'path: ')
@click.option("--file_name")

def file_search(path, file_name):
    results = glob.glob(f"{path}  {file_name}")




if __name__ =="__main__":
    file_search()

