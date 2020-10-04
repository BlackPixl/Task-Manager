import arguments
import processes

args = arguments.args()

print(args)

new_process = args.get("new")
kill_process = args.get("kill")

if new_process:
    processes.create_process(new_process)

if args.pop("list"):
    processes.list_processes()
    
if kill_process:
    processes.kill_process(kill_process)
