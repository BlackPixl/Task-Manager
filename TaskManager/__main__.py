# -*- coding: utf-8 -*-
import subprocess as sp


def main():
    flag = True

    while flag:
        get_welcome()
        flag = ask()


def print_array_contents(array):
    for i in range(0, len(array)):
        element = array[i]
        print("->" + element)
    print('------------------------\n')


def get_process():
    processes_bin = sp.check_output("ps -e -o pid,ppid,comm,user", shell=True)
    processes = processes_bin.decode('UTF-8')
    processes_list = processes.split('\n')

    for proc in processes_list:
        print(proc)

    print('------------------------')


def create_process(name_proc):
    try:
        sp.Popen([name_proc])
    except FileNotFoundError:
        print('Application not found')


def get_welcome():
    print('Welcome to TaskManager')
    print('------------------------\n')


def spawn_process():
    app_name = str(input("Type the name of the app\n>>"))
    create_process(app_name)


def kill_process():
    PID = input('Write the PID of the process to kill: ')
    sp.check_output(f"kill {PID}", shell=True)
    print(f'Process {PID} killed successfully\n')


def refresh_console():
    sp.run("clear", shell=True)
    get_process()


def get_users():
    users = sp.check_output("ps -A -o user | sort | uniq", shell=True)
    decoded_users = users.decode('UTF-8')
    users_list = decoded_users.split('\n')
    users_list.pop()
    return users_list


def child_sleep():
    x = sp.Popen("sleep 1000 &", shell=True)
    y = x.pid
    print(f"the PID of the new child process is {y + 1} \n")


def ask():
    res = ''

    while res != 'Q':
        print('Press 1 to spawn a process.')
        print('Press 2 to kill a task.')
        print('Press 3 to see the number of open tasks.')
        print('Press 4 to show all running tasks.')
        print('Press 5 to see the users.')
        print('Press 6 to see the running task for a given user.')
        print('Press 7 to create a child process.')
        res = input('To exit press "Q". \n>> ')

        if res == '1':
            spawn_process()

        elif res == '2':
            kill_process()

        elif res == '3':
            n = sp.check_output("ps aux | wc -l", shell=True)
            n = n.decode('UTF-8')
            print(f'Number of tasks: {n}')

        elif res == '4':
            refresh_console()

        elif res == '5':
            usr_list = get_users()
            print_array_contents(usr_list)

        elif res == '6':
            usr_list = get_users()
            selUser = input('Select the user \n')
            if selUser in usr_list:
                sp.run(f"ps -U {selUser} -u {selUser} -o pid,ppid,comm,user", shell=True)
            else:
                print('User not found')
        elif res == '7':
            child_sleep()

        elif res == 'Q':
            print('Good Bye!!')
            return False

        else:
            print('command not recognized.\n')


main()
