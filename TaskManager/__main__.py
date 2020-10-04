import arguments
import processes

args = arguments.args()

print(args)  # this prints the arguments given to the script, test only.

new_process = args.get("new")

if new_process:
    print(processes.create_process(new_process))

if args.pop("list"):
    processes.list_processes()
