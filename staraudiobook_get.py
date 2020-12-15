# -*- coding: utf-8 -*-
__version__ = "0.01.0"
"""
Source : https://github.com/izneo-get/staraudiobook-get

Script pour sauvegarder les livres de staraudiobook.com
"""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import unquote
import sys
import re


def check_version():
    latest_version_url = 'https://raw.githubusercontent.com/izneo-get/staraudiobook-get/master/VERSION'
    res = requests.get(latest_version_url)
    if res.status_code != 200:
        print(f"Version {__version__} (impossible de vérifier s'il existe une version plus récente)")
    else:
        latest_version = res.text.strip()
        if latest_version == __version__:
            print(f"Version {__version__} (la plus récente)")
        else:
            print(f"Version {__version__} (il existe une version plus récente : {latest_version})")
            print("https://github.com/izneo-get/staraudiobook-get/releases")


def download_book(url, folder='.'):
    pages_to_download = [url]

    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')

    elems = soup.find_all("a", class_="post-page-numbers")
    for e in elems:
        page = e.attrs['href']
        pages_to_download.append(page)

    for u in pages_to_download:
        if u != url:
            response = requests.request("GET", u)
            soup = BeautifulSoup(response.text, 'html.parser')
        elems = soup.find_all("audio")
        for e in elems:
            src = e.find("a").attrs['href']
            file_name = unquote(src.split("/")[-1])
            print(f"{file_name}")
            os.makedirs(folder, exist_ok=True)
            my_file = open(f"{folder}/{file_name}", 'wb')
            resp = requests.get(src, stream=True)
            expected_size = int(resp.headers['Content-length'])
            downloaded_size = 0
            if resp.status_code != 200:
                print('not 200!')
                print(resp)
                print(src)
                break
            for chunk in resp:
                my_file.write(chunk)
                my_file.flush()
                downloaded_size += len(chunk)
                print(f"{downloaded_size // 1024} / {expected_size // 1024} [{(downloaded_size * 100 // expected_size)} %]", end="\r")
            my_file.close()
            print("")


if __name__ == "__main__":
    output_folder = "DOWNLOADS"

    check_version()

    # Récupération de l'URL du livre souhaité (si pas en argument, on le demande).
    book_urls = ""
    if len(sys.argv) > 1:
        book_urls = " ".join(sys.argv[1:])
    while book_urls.upper() != "Q" and not re.match(
        "https://staraudiobook.com/(.+)", book_urls
    ):
        book_urls = input(
            'URL de la publication au format "https://staraudiobook.com/{title}/" ("Q" pour quitter) : '
        )

    if book_urls.upper() == "Q":
        sys.exit()

    for book_url in book_urls.split(" "):
        folder = book_url.split("/")[-1] if book_url.split("/")[-1] else book_url.split("/")[-2]
        folder = output_folder + '/' + folder
        print(f"Téléchargement de \"{book_url}\" dans \"{folder}\"")
        download_book(book_url, folder)

    if len(sys.argv) == 1:
        # Mode interactif.
        os.system("pause")