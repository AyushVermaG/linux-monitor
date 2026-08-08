import os
import time
from datetime import datetime

from modules.cpu import get_cpu_usage
from modules.memory import get_memory_usage
from modules.disk import get_disk_usage
from modules.processes import get_top_processes


def make_bar(percent, length=20):
    filled = int(percent / 100 * length)
    return "#" * filled + "-" * (length - filled)


while True:
    # Clear terminal
    os.system("clear")

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    processes = get_top_processes()

    print("ProcWatch - Real-Time Linux Monitor")
    print("=" * 45)

    print(f"CPU Usage    : {cpu}%")
    print(f"[{make_bar(cpu)}]")

    print()

    print(f"Memory Usage : {memory['used_gb']} GB / {memory['total_gb']} GB")
    print(f"[{make_bar(memory['percent'])}] {memory['percent']}%")

    print()

    print(f"Disk Usage   : {disk['used_gb']} GB / {disk['total_gb']} GB")
    print(f"[{make_bar(disk['percent'])}] {disk['percent']}%")

    print()
    print("Top Processes")
    print("-" * 45)
    print(f"{'PID':<8}{'NAME':<20}{'CPU%':>8}")
    print("-" * 45)

    for p in processes:
        print(f"{p['pid']:<8}{p['name']:<20}{p['cpu']:>8}")

    print()
    print(f"Updated: {datetime.now().strftime('%H:%M:%S')}")
    print("Refreshing every 10 seconds...")

    time.sleep(10)