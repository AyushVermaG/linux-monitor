import os

def get_disk_usage(path="/"):
    stat = os.statvfs(path)

    total = stat.f_frsize * stat.f_blocks
    free = stat.f_frsize * stat.f_bavail
    used = total - free

    percent = (used / total) * 100

    return {
        "total_gb": round(total / (1024**3), 2),
        "used_gb": round(used / (1024**3), 2),
        "percent": round(percent, 2)
    }