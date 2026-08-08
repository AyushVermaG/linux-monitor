# Linux System Monitoring Dashboard

A modular Python command-line tool that displays real-time Linux system statistics.

## Features

- CPU usage monitoring from `/proc/stat`
- Memory usage from `/proc/meminfo`
- Disk usage using `df`
- Top CPU-consuming processes using `ps`
- Terminal progress bars for quick visualization

## Project Structure

```text
linux-monitor/
├── modules/
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── processes.py
│   └── uptime.py
├── monitor.py
└── README.md
```

## Run

```bash
python3 monitor.py
```

## Tech Stack

Python · Linux · Bash · /proc filesystem

This project was built to understand how Linux exposes system information and how to create a lightweight terminal-based monitoring dashboard without external Python libraries.
