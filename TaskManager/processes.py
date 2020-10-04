def list_processes():
    processes_bin = sp.check_output("ps -e -o pid,ppid,comm,user",shell=True)
    processes = processes_bin.decode('UTF-8')
    processes_list = processes.split('\n')

    for proc in processes_list:
        print(proc)


def create_process(process):
    return process
