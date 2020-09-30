import arguments


def list_processes():
    return 'TestPrintProcesses'


def create_process(process):
    return process


args = arguments.args()

print(args)

new_process = args.get("new")
if new_process:
    print(create_process(new_process))

if args.pop("list"):
    print(list_processes())
