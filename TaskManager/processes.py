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
        print(f'Process {pid} deleted succesfully\n')
    except sp.CalledProcessError:
        print('Process not found')

    print('printing current processes...')
    time.sleep(3)
    list_processes()
