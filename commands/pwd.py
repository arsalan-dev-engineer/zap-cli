import click
import commands.password_search as password

@click.group()
def pwd():
    pass

@pwd.command("search", help="""
                            This is a text file.
                            """)
@click.option("-u", "--url", required=True, type=str, help="Input url")
def query_url(url):
    password.load_json_files(url)

if __name__ == "__main__":
    pwd()
