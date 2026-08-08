import subprocess
import os

def get_top_processes(limit=5):
    current_pid = str(os.getpid())

    result = subprocess.check_output(
        "ps -eo pid,comm,%cpu --sort=-%cpu",
        shell=True,
        text=True
    )

    lines = result.strip().split("\n")[1:]

    processes = []

    for line in lines:
        parts = line.split(None, 2)

        if len(parts) == 3:
            pid, name, cpu = parts

            # Skip the monitor itself and the ps command
            if pid == current_pid or name == "ps":
                continue

            processes.append({
                "pid": pid,
                "name": name,
                "cpu": cpu
            })

        if len(processes) == limit:
            break

    return processes