import json
import re
from urllib import parse
import click
import requests


@click.command()
@click.argument("url", nargs=1, type=click.STRING)
def yadisk_ddl(url):
    response = requests.get(url)

    yandexuid = response.cookies.get("yandexuid")

    pattern = re.compile(r"\"hash\":\"(?P<hash>.+?)\"")
    match = re.search(pattern, str(response.content))
    hash = match["hash"]

    pattern = re.compile(r"\"sk\":\"(?P<sk>.+?)\"")
    match = re.search(pattern, str(response.content))
    sk = match["sk"]

    payload = parse.quote(json.dumps({
        "hash": hash,
        "sk": sk,
        "options": {
            "hasExperimentVideoWithoutPreview": True
        }
    }))
    response = requests.post(
        "https://yadi.sk/public/api/download-url",
        data = payload,
        headers = {
            "Content-Type": "text/plain"
        },
        cookies = {
            "yandexuid": yandexuid
        }
    )

    url = response.json()["data"]["url"]
    click.echo(url)


if __name__ == "__main__":
    yadisk_ddl()
