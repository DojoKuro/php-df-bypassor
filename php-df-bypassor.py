#!/usr/bin/python3
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument(
    "-u", "--url", help="PHPinfo URL: eg. https://example.com/phpinfo.php"
)
parser.add_argument("-f", "--file", help="PHPinfo localfile path: eg. dir/phpinfo")

args = parser.parse_args()


class colors:
    reset = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"


print(
    colors.green
    + f"""
     _  __     _                                   
  __| |/ _|___| |__ _  _ _ __  __ _ ______ ___ _ _ 
 / _` |  _|___| '_ \ || | '_ \/ _` (_-<_-</ _ \ '_|
 \__,_|_|     |_.__/\_, | .__/\__,_/__/__/\___/_|  
                    |__/|_|                        
"""
    + f"\n\t\t\t"
    + colors.blue
    + f"by: "
    + colors.orange
    + f"DojoKuro"
    + f"\n"
    + colors.reset
)

if args.url:
    url = args.url
    phpinfo = requests.get(url).text

elif args.file:
    phpinfofile = args.file
    phpinfo = open(phpinfofile, "r").read()

else:
    print(parser.print_help())
    exit()

inp = []

inp = (
    phpinfo.split('disable_functions</td><td class="v">')[1]
    .split("</")[0]
    .split(",")[:-1]
)

dangerous_functions = [
    "pcntl_alarm",
    "pcntl_fork",
    "pcntl_waitpid",
    "pcntl_wait",
    "pcntl_wifexited",
    "pcntl_wifstopped",
    "pcntl_wifsignaled",
    "pcntl_wifcontinued",
    "pcntl_wexitstatus",
    "pcntl_wtermsig",
    "pcntl_wstopsig",
    "pcntl_signal",
    "pcntl_signal_get_handler",
    "pcntl_signal_dispatch",
    "pcntl_get_last_error",
    "pcntl_strerror",
    "pcntl_sigprocmask",
    "pcntl_sigwaitinfo",
    "pcntl_sigtimedwait",
    "pcntl_exec",
    "pcntl_getpriority",
    "pcntl_setpriority",
    "pcntl_async_signals",
    "error_log",
    "system",
    "exec",
    "shell_exec",
    "popen",
    "proc_open",
    "passthru",
    "link",
    "symlink",
    "syslog",
    "ld",
    "mail",
]

exploitable_functions = []

for i in dangerous_functions:
    if i not in inp:
        exploitable_functions.append(i)

if len(exploitable_functions) == 0:
    print("\nThere is no Non-disabled function.")

else:
    print("\nNon-disabled functions list:")
    print(colors.red + ",".join(exploitable_functions) + colors.reset)
