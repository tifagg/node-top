# node-top

`top` for Node.js processes.

Real-time CPU, memory, and process stats directly in your terminal.

---

## What is this?

`node-top` is an experimental terminal dashboard for monitoring running Node.js processes on your machine.

Think `htop`, but focused entirely on Node workloads.

Track which scripts are eating RAM, inspect CPU usage, monitor uptime, and eventually detect event loop lag before your laptop starts sounding like a drone strike.

Built for developers tired of:

```bash
ps aux | grep node
```

and wanting actual visibility into their runtime.

---

## Planned Features

- Live Node.js process list
- CPU and memory monitoring
- Heap / RSS breakdown
- Event loop lag detection
- Interactive process controls
- Cross-platform terminal UI
- Dev environment awareness (`nodemon`, `next dev`, etc.)

---

## Current Status

Early experimental prototype.

---

## Tech Stack

- Python
- psutil
- colorama

---

## Installation

```bash
git clone https://github.com/TeefsVault/node-top.git
cd node-top
pip install -r requirements.txt
python node-top.py
```

---

## Vision

A lightweight developer-focused terminal monitor with the feel of:
- `htop`
- `btop`
- `nvtop`

...but specialized for Node.js runtimes and developer workflows.
