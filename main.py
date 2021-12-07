import os
import sys
import requests, random, time, json
from colorama import Fore, init
from base64 import b64decode, b64encode
from urllib.request import Request, urlopen
messages = []
counter = 0
lines = []
usrcount = 696969
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token checker made by {Fore.WHITE}Blaze{Fore.LIGHTBLACK_EX}, support me via cashapp {Fore.WHITE}$BlazeStackdev{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}my github: {Fore.WHITE}https://github.com/Blaze-stack")

    
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

def usrgrab():
    usrs = []
    toks = []
    working = []
    checked = []
    already_cached_tokens = []

    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            usr = username
            tks = token

            users.append(usr)
            toks.append(tks)
            
    print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX} Pick the username to fine the token of, ")

    for i in range(len(uses)):
        choice = input(f'{Fore.GREEN}>{Fore.RESET} is it {users[i]} [y/n]')

        if choice.lowwer() == "y":
            usrcount = i
            print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX} looking for token... ")
            break
        else:
            pass

    if usercount == 696969:
        print(f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No tokens where found. {Fore.WHITE} Error 506. {Fore.WHITE}")
    else:
        token = toks[usercount]
        print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX} Token found! {token}")

usrgrab()