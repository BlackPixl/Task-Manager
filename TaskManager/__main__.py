import arguments
import processes

args = arguments.args()

print(args)

new_process = args.get("new")

if new_process:
    print(processes.create_process(new_process))

if args.pop("list"):
    print(processes.list_processes())
