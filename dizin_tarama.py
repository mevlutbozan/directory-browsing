import requests
from concurrent.futures import ThreadPoolExecutor
import argparse

def dizin_tarama(url, kelime):
    hedef = f"{url}/{kelime}"
    try:
        yanit = requests.get(hedef)
        if yanit.status_code == 200:
            print(f"[+] Bulundu: {hedef} - {yanit.status_code}")
    except requests.RequestException as e:
        print(f"[-] Hata: {e}")

def dirbuster(url, wordlist):
    with ThreadPoolExecutor(max_workers=50) as executor:
        with open(wordlist, 'r') as file:
            for kelime in file:
                kelime = kelime.strip()
                executor.submit(dizin_tarama, url, kelime)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python DirBuster")
    parser.add_argument("url", help="Hedef URL")
    parser.add_argument("wordlist", help="Wordlist dosya yolu")
    args = parser.parse_args()

    dirbuster(args.url, args.wordlist)
