# Raspberry Pi Zero 2 W – Headless Linux Server (Homelab)

This documents my process of turning a Raspberry Pi Zero 2 W into a
headless Linux server that I can manage entirely over SSH, without a monitor or keyboard.

The goal of this project is to understand how real servers are set up, managed,
and run in practice — not just how to write application code.

---

## What I built
- Flashed Raspberry Pi OS Lite (64-bit)
- Configured Wi-Fi and SSH using Raspberry Pi Imager
- Set up a fully headless Raspberry Pi (no display, no peripherals)
- Connected and managed the device remotely from Windows via SSH
- Performed system updates and basic hardening
- Created a Python virtual environment for isolated development
- Deployed a Discord bot as a managed Linux service using systemd

---

## Why this project
I want to build real-world systems, not just scripts that run once.

This setup is meant to act as a small personal homelab that I can use to:
- host long-running services
- experiment with backend infrastructure
- deploy bots and APIs
- later integrate AI-powered features using cloud-based models

This project focuses more on **infrastructure, deployment, and reliability**
than on pure application logic.

---

## Tech stack
- Raspberry Pi Zero 2 W  
- Raspberry Pi OS Lite (64-bit)  
- Linux  
- SSH  
- systemd  
- Python  
- Virtual environments (venv)  

---

## Things I learned
- How SSH works and how headless servers are managed
- How Linux services boot and run without user interaction
- Navigating and managing a Linux system remotely
- Using Python virtual environments and pip for dependency isolation
- Async and event-driven programming concepts
- API authentication and permission models
- Debugging real runtime errors using logs and tracebacks
- The difference between configuration issues and code bugs
- Running Python applications as persistent system services

---

## Problems I ran into
- SSH hostname not resolving on Windows
- First-boot SSH disconnects
- Python modules not found due to inactive virtual environments
- Environment variables not persisting across sessions
- Managing application restarts without manual intervention

---

## How I solved them
- Connected using the device IP instead of `raspberrypi.local`
- Waited for initial boot processes to complete
- Properly activated virtual environments
- Moved secrets to environment variables
- Used systemd to manage the application lifecycle

---

## Next steps
- Add data persistence using SQLite
- Expand the Discord bot with admin-level commands
- Expose simple backend APIs
- Use this setup as a base for future AI-integrated services

---

## Status
🚧 Work in progress
