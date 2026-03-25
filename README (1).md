# 🔍 Python Port Scanner

A lightweight command-line tool built with Python that scans ports 1–1024 on a target host and identifies which ones are open. Built as a hands-on learning project to explore the fundamentals of networking and cybersecurity.

---

## 📋 Description

The Python Port Scanner connects to a target IP address or hostname and systematically probes each port in the range 1–1024, reporting back which ports are open and potentially accepting connections. This type of tool is a staple in any security professional's toolkit and is commonly used for network reconnaissance and vulnerability assessment.

> ⚠️ **Disclaimer:** This tool is intended for educational purposes only. Only scan systems you own or have explicit permission to test. Unauthorized port scanning may be illegal in your jurisdiction.

---

## ✨ Features

- Scans all **well-known ports** (1–1024) on a target host
- Displays **open ports** clearly in the terminal output
- Uses Python's built-in `socket` library — no external dependencies
- Handles **connection timeouts** gracefully to avoid hanging on closed ports
- Shows **scan start and end time** for basic performance tracking
- Clean, readable command-line output

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| `socket` | Low-level networking and TCP connection handling |
| `datetime` | Tracking scan start and end times |

---

## 🚀 How to Run

### Prerequisites

- Python 3.x installed on your machine
- A terminal or command prompt

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/your-username/python-port-scanner.git
cd python-port-scanner
```

**2. Run the scanner**

```bash
python port_scanner.py
```

**3. Enter the target host when prompted**

```
Enter the target IP or hostname: 127.0.0.1
```

**4. View the results**

```
--------------------------------------------------
Scanning target: 127.0.0.1
Scan started at: 2024-01-15 10:32:00
--------------------------------------------------
[*] Port 22  is OPEN
[*] Port 80  is OPEN
[*] Port 443 is OPEN
--------------------------------------------------
Scan completed in 12.4 seconds.
--------------------------------------------------
```

> 💡 **Tip:** You can scan your own machine by using `127.0.0.1` (localhost) as the target. This is a safe way to test the tool.

---

## 📚 What I Learned

Working on this project gave me hands-on experience with several important concepts:

- **Networking fundamentals** — Understanding how TCP connections work, what ports are, and how clients and servers communicate
- **Python's `socket` library** — How to create sockets, set timeouts, and attempt connections programmatically
- **Port ranges and well-known services** — The significance of ports 1–1024 and how common services (SSH, HTTP, HTTPS) map to specific port numbers
- **Error handling** — Managing exceptions like `ConnectionRefusedError` and `socket.timeout` to distinguish between closed and filtered ports
- **Basic reconnaissance concepts** — How port scanning is used in real-world cybersecurity assessments and penetration testing

---

## 🔮 Future Improvements

Here are some features I plan to add as I continue learning:

- [ ] **Service detection** — Identify which service (e.g., HTTP, FTP, SSH) is running on each open port
- [ ] **Custom port ranges** — Allow the user to specify a custom range instead of only 1–1024
- [ ] **Multi-threading** — Speed up the scan significantly using concurrent threads
- [ ] **Banner grabbing** — Retrieve service banners from open ports for more detailed information
- [ ] **Output to file** — Save scan results to a `.txt` or `.csv` file
- [ ] **UDP scanning** — Extend support beyond TCP to scan UDP ports as well
- [ ] **Command-line arguments** — Accept target and options via `argparse` instead of interactive prompts

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with curiosity and lots of `print()` statements 🐍*
