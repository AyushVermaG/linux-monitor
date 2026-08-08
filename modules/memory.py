def get_memory_usage():
    meminfo = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":")
            meminfo[key] = int(value.strip().split()[0])

    total = meminfo["MemTotal"]
    available = meminfo["MemAvailable"]
    used = total - available

    usage_percent = (used / total) * 100

    return {
        "total_gb": round(total / 1024 / 1024, 2),
        "used_gb": round(used / 1024 / 1024, 2),
        "percent": round(usage_percent, 2)
    }