import subprocess as sp

def list_processes():
    processes_bin = sp.check_output("ps -e -o pid,ppid,comm,user",shell=True)
    processes = processes_bin.decode('UTF-8')
    processes_list = processes.split('\n')

    for proc in processes_list:
        print(proc)


def create_process(process):
    return process
    
def kill_process(pid):
    kill = sp.check_output(f"kill {pid}",shell=True)
    print(f'Process {pid} deleted succesfully\n')
