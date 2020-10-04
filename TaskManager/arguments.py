from argparse import ArgumentParser


def args():
    parser = ArgumentParser(description="A simple console app which allows you to monitor and manage system processes",
                            usage="\nUse -ls to list all the processes running in the system."
                                  "\nUse -n <process> to start a new process.\n")

    parser.add_argument("-ls",
                        action='store_true',
                        help='lists all running processes')

    parser.add_argument("-n",
                        type=str,
                        help='Creates a new process')


    parser.add_argument("-k",
                        type=str,
                        help='Kill a process with given PID')

    arguments = parser.parse_args()

    return {
        "list": arguments.ls,
        "new": arguments.n,
        "kill": arguments.k
    }
