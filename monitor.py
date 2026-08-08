from modules.cpu import get_cpu_usage
from modules.memory import get_memory_usage
from modules.disk import get_disk_usage

cpu = get_cpu_usage()
memory = get_memory_usage()
disk = get_disk_usage()

def make_bar(percent, length=20):
    filled = int(percent / 100 * length)
    return "#" * filled + "-" * (length - filled)

print("Linux System Monitor")
print("=" * 40)

print(f"CPU Usage    : {cpu}%")
print(f"[{make_bar(cpu)}]")

print()

print(f"Memory Usage : {memory['used_gb']} GB / {memory['total_gb']} GB")
print(f"[{make_bar(memory['percent'])}] {memory['percent']}%")

print()

print(f"Disk Usage   : {disk['used_gb']} GB / {disk['total_gb']} GB")
print(f"[{make_bar(disk['percent'])}] {disk['percent']}%")