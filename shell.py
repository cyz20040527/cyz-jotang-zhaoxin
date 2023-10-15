import shlex
def parse_command(command):
    # 使用shlex模块解析命令行输入
        split_command = shlex.split(command)
        return split_command

import subprocess
def execute_command(command):
    # 使用subprocess执行命令
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(f"Error: {error.decode()}")
    else:
        print(output.decode())

import os
HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".yourshellname_history")
def save_history(command):
    with open(HISTORY_FILE, "a") as f:
        f.write(command + "\n")

import os
def exit_shell():
    # 退出shell
    os._exit(0)

import os
def expand_path(path):
    # 解析路径
    if path == "~":
        return os.path.expanduser("~")
    elif path == ".-":  # 当前目录和上一级目录的快捷方式
        return os.path.join(os.getcwd(), "../")
    else:
        return path
