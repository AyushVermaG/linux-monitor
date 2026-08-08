import time


def read_cpu_times():
    with open("/proc/stat", "r") as file:
        line = file.readline()

    values = line.split()[1:]
    values = [int(v) for v in values]

    idle = values[3] + values[4]   # idle + iowait
    total = sum(values)

    return idle, total


def get_cpu_usage():
    idle1, total1 = read_cpu_times()

    time.sleep(1)

    idle2, total2 = read_cpu_times()

    idle_diff = idle2 - idle1
    total_diff = total2 - total1

    usage = 100 * (1 - idle_diff / total_diff)

    return round(usage, 2)