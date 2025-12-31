# pi-zero-2w-homelab
# Raspberry Pi Zero 2 W – Headless Server Setup

This repository documents my journey of setting up a Raspberry Pi Zero 2 W
as a headless Linux server using SSH.

## What I did
- Flashed Raspberry Pi OS Lite (64-bit)
- Configured Wi-Fi and SSH using Raspberry Pi Imager
- Set up a headless Raspberry Pi (no screen, no keyboard)
- Connected via SSH from Windows
- Performed initial system updates

## Why this project
I want to build real-world systems, not just write code.
This setup will later be used to host:
- a Discord bot
- small backend services
- future AI-related experiments

## Tech stack
- Raspberry Pi Zero 2 W
- Raspberry Pi OS Lite (64-bit)
- Linux
- SSH
- Python (coming next)
- ## Things I learned
- What SSH is and how it works
- How headless servers are managed
- How Linux servers boot and connect to Wi-Fi
- Basic Linux commands

## Problems faced
- SSH hostname not resolving on Windows
- First-boot SSH disconnects

## How I solved them
- Used IP address instead of raspberrypi.local
- Waited for first boot to finish
## Status
🚧 Work in progress
