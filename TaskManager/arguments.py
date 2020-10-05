from argparse import ArgumentParser


def args():
    parser = ArgumentParser(description="A simple console app which allows you to monitor and manage system processes",
                            usage="\nUse -ls to list all the processes running in the system."
                                  "\nUse -n <process> to start a new process."
                                  "\nUse -k <PID> to kill a process."
                                  "\nUse -u to list all users."
                                  "\nUse -lsu <user> to list all processes associated to a user")

    parser.add_argument("-ls",
                        action='store_true',
                        help='Lists all running processes')

    parser.add_argument("-n",
                        type=str,
                        help='Creates a new process')

    parser.add_argument("-k",
                        type=str,
                        help='Kill a process with given PID')

    parser.add_argument("-u",
                        action='store_true',
                        help='List all users')

    parser.add_argument("-lsu",
                        type=str,
                        help='Lists all running processes from a given user')

    arguments = parser.parse_args()

    return {
        "list": arguments.ls,
        "new": arguments.n,
        "kill": arguments.k,
        "list_users": arguments.u,
        "list_proc_user": arguments.lsu
    }
