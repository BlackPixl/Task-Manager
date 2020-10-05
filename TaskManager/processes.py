import subprocess as sp
import time

def list_processes():
    processes_bin = sp.check_output("ps -e -o pid,ppid,comm,user", shell=True)
    processes = processes_bin.decode('UTF-8')
    processes_list = processes.split('\n')
    processes_list.pop()  # deletes the last element which is an empty string

    for proc in processes_list:
        print(proc)


def create_process(process):
    try:
        sp.Popen([process])
    except FileNotFoundError:
        print('Application not found')


def kill_process(pid):
    try:
        sp.check_output(f"kill {pid}", shell=True)
        print(f'Process {pid} deleted successfully\n')
    except sp.CalledProcessError:
        print('Process not found')

    print('printing current processes...')
    time.sleep(3)
    list_processes()


def list_users():
    users = sp.check_output("ps -A -o user | sort | uniq", shell=True)
    users1 = users.decode('UTF-8')
    users_list = users1.split('\n')
    users_list.pop()

    if "USER" in users_list:
        users_list.remove("USER")

    print('------------------------')

    for i in range(0, len(users_list)):
        user2 = users_list[i]
        print(f"- " + user2)

    print('------------------------\n')


def list_proc_user(user):
    show_process = sp.run(f"ps -U {user} -u {user} -o pid,ppid,comm,user", shell=True)
    if show_process.returncode == 1:
        print('\nUser not found')
        print('Users in the system:\n')
        list_users()
