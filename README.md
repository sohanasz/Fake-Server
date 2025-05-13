# Fake-Server
This is a minimal TCP server built using Python’s socket module. It listens on a user-defined IP and port, simulating an open port on your local machine or network. This project is particularly useful for testing and demonstrating how port scanners and network monitoring tools detect open ports.

## 📦 What It Does

- Binds to a user-defined port (default: 5050)
- Listens for incoming TCP connections
- Sends a simple message (`"Hello!"`) on connection
- Can be used alongside tools like port scanners

## 🚀 How to Run

```bash
python fake_server.py
