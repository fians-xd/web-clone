import os
import time
import sys

# ANSI color codes
c = '\x1b[38;5;172m'  # cyan
pn = '\x1b[38;5;86m'   # light green
kt = '\x1b[1;33m'      # bold yellow
bt = '\x1b[36;1m'      # bold cyan
m = '\x1b[31;1m'       # bold red
n = '\x1b[0;0m'        # reset


# Logo
logo = f"""    _   _           _         ____        _   
   | | | | ___  ___| |_ __ _ / ___|  ___ | |_ 
   | |_| |/ _ \/ __| __/ _` | |  _  / _ \| __|
   |  _  |  __/\__ \ || (_| | |_| || (_) | |_ 
   |_| |_|\___||___/\__\__,_|\____(_)___/ \__| V-1.0

{kt}INI ADALAH SEBUAH PROGRAM UNTUK BACKUP WEBSITE YANG SEDERHANA\n{n}"""

# Function for slow printing
def print_slow(text, delay=0.001, color=""):
    for char in text:
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(delay)

# Menu
menu = f"""
{bt}Menu:{n}
1. {bt}Cloning no login{n}
2. {bt}Cloning Login{n}
3. {bt}Cloning Login+Cookie+Header{n}
"""

os.system("clear")
print_slow(logo, delay=0.001)
print(menu)
choice = input(f"{kt}Silahkan pilih menu nya: {n}")

# Notes
note1 = f"""
{c}note:{n}
{pn}cara ini khusus buat website yang tidak ada user login nya..!!{n}
"""

note2 = f"""
{c}note:{n}
{pn}Cara ini menggunakan cookie{n}
1. {pn}login dulu ke website nya{n}
2. {pn}Seperti biasa ambil cookie nya{n}
3. {pn}Usahakan selesaikan captcha nya sebelum login jika ada{n}
4. {pn}karena captcha juga termasuk sesi wajib sebelum ambil cookie{n}
5. {pn}terserah ambil cookie nya menggunakan tools apa{n}
6. {pn}masukan kedalam file cookie.txt untuk login{n}
7. {pn}Isi user agent yang digunakan untuk sesi login (untuk header agar berhasil){n}
"""

note3 = f"""
{c}note:{n}
{pn}Cara ini menggunakan cookie{n}
1. {pn}login dulu ke website nya{n}
2. {pn}Seperti biasa ambil cookie nya{n}
3. {pn}Usahakan selesaikan captcha nya sebelum login jika ada{n}
4. {pn}karena captcha juga termasuk sesi wajib sebelum ambil cookie{n}
5. {pn}terserah ambil cookie nya menggunakan tools apa{n}
6. {pn}ambil juga header yang dibutuhkan inputan ini{n}
7. {pn}masukan kedalam file cookie.txt untuk login{n}
8. {pn}Isi user agent yang digunakan untuk sesi login (untuk header agar berhasil){n}
"""


if choice == '1':
    print_slow(note1)
    url = input(f"{kt}Masukkan URL: {n}")
    command = f"wget --mirror --convert-links --adjust-extension --page-requisites --no-parent --execute robots=off --wait=1 --random-wait '{url}'"
    print(f"\n{m}Menjalankan perintah: {command}{n}")
    os.system(command)

elif choice == '2':
    print_slow(note2)
    url = input(f"{kt}Masukkan URL: {n}")
    username = input(f"{kt}Masukkan Username: {n}")
    password = input(f"{kt}Masukkan Password: {n}")
    cookie_file = input(f"{kt}Masukkan file cookie: {n}")
    user_agent = input(f"{kt}Masukkan User-Agent: {n}")
    command = (
        f"wget --mirror --user={username} --password={password} --load-cookies {cookie_file} "
        f"--convert-links --adjust-extension --page-requisites --no-parent "
        f"--execute robots=off --wait=1 --random-wait --header=\"User-Agent: {user_agent}\" '{url}'"
    )
    print(f"\n{m}Menjalankan perintah: {command}{n}")
    os.system(command)

elif choice == '3':
    print_slow(note3)
    url = input(f"{kt}Masukkan URL: {n}")
    username = input(f"{kt}Masukkan Username: {n}")
    password = input(f"{kt}Masukkan Password: {n}")
    cookie_file = input(f"{kt}Masukkan file cookie: {n}")
    user_agent = input(f"{kt}Masukkan User-Agent: {n}")
    referer = input(f"{kt}Masukkan Referer: {n}")
    accept = input(f"{kt}Masukkan Accept header: {n}")
    accept_language = input(f"{kt}Masukkan Accept-Language: {n}")
    authorization = input(f"{kt}Masukkan Authorization header: {n}")
    command = (
        f"wget --mirror --user={username} --password={password} --load-cookies {cookie_file} "
        f"--convert-links --adjust-extension --page-requisites --no-parent "
        f"--execute robots=off --wait=1 --random-wait --header=\"User-Agent: {user_agent}\" "
        f"--header=\"Referer: {referer}\" --header=\"Accept: {accept}\" "
        f"--header=\"Accept-Language: {accept_language}\" --header=\"Authorization: {authorization}\" '{url}'"
    )
    print(f"\n{m}Menjalankan perintah: {command}{n}")
    os.system(command)

else:
    print(f"{m}Pilihan tidak valid. Silakan coba lagi.{n}")
