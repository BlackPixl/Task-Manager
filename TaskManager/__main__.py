import arguments
import processes

args = arguments.args()

if not any(args.values()):
    print("No arguments provided.\n"
          "Usage: TaskManager [options]\n\n"
          "Try 'TaskManager -h'\n"
          "For additional help.\n")

new_process = args.get("new")
kill_process = args.get("kill")
user_proc = args.get("list_proc_user")

if new_process:
    processes.create_process(new_process)

if kill_process:
    processes.kill_process(kill_process)

if user_proc:
    processes.list_proc_user(user_proc)

if args.pop("list_users"):
    processes.list_users()

if args.pop("list"):
    processes.list_processes()
