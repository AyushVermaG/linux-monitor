from modules.cpu import get_cpu_usage
from modules.memory import get_memory_usage

cpu = get_cpu_usage()
memory = get_memory_usage()

bar_length = 20
filled = int(memory["percent"] / 100 * bar_length)
bar = "#" * filled + "-" * (bar_length - filled)

print("Linux System Monitor")
print("-" * 30)
print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory['used_gb']} GB / {memory['total_gb']} GB")
print(f"[{bar}] {memory['percent']}%")