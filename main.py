import urllib.request
from datetime import datetime

start = "# GitHub520 Host Start\n"
end = "# GitHub520 Host End\n"


def solve_hosts():
    with open("/etc/hosts") as f:
        lines: list = f.readlines()
    if start in lines and end in lines:
        write_exist(lines)
    else:
        write_none(lines)


def write_exist(lines):
    s = lines.index(start)
    e = lines.index(end)
    lines = lines[0:s] + lines[e + 1:]
    if "\n" not in lines[-1]:
        lines[-1] = lines[-1] + "\n"
    new_hosts = get_hosts()
    lines += new_hosts

    with open("/etc/hosts", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)


def write_none(lines):
    new_hosts = get_hosts()
    if "\n" not in lines[-1]:
        lines[-1] = lines[-1] + "\n"
    lines = lines + new_hosts

    with open("/etc/hosts", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)


def get_hosts():
    host_file = urllib.request.urlopen('https://raw.hellogithub.com/hosts')
    new_hosts = host_file.read().decode("utf8").split("\n")
    new_hosts = list(map(lambda x: x + "\n", new_hosts))
    return new_hosts


if __name__ == "__main__":
    print(f"=============执行开始:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}===========")
    solve_hosts()
    print(f"=============执行结束:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}===========")
    print("\n")
