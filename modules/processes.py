import subprocess

def get_top_processes(limit=5):
    result = subprocess.check_output(
        ["ps", "-eo", "pid,comm,%cpu", "--sort=-%cpu"],
        text=True
    )

    lines = result.strip().split("\n")[1:limit+1]

    processes = []

    for line in lines:
        parts = line.split(None, 2)
        if len(parts) == 3:
            pid, name, cpu = parts
            processes.append({
                "pid": pid,
                "name": name,
                "cpu": cpu
            })

    return processes