# Local Development Setup

This document explains how to set up the Restaurant Multi-Agent Order Management System for local development.

---

# Prerequisites

Before running the project, make sure the following software is installed:

- Python 3.12+
- Git
- WSL (Ubuntu)
- Prosody XMPP Server
- Visual Studio Code (recommended)

---

# Clone the Repository

```bash
git clone https://github.com/<your-username>/Restaurant-Multi-Agent-Order-Management-System.git

cd Restaurant-Multi-Agent-Order-Management-System
```

---

# Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

**PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Command Prompt**

```cmd
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Prosody (WSL)

Update Ubuntu:

```bash
sudo apt update
sudo apt upgrade
```

Install Prosody:

```bash
sudo apt install prosody
```

Verify installation:

```bash
sudo systemctl status prosody
```

---

# Configure Prosody

Create a VirtualHost configuration:

```bash
sudo nano /etc/prosody/conf.d/localhost.cfg.lua
```

Add:

```lua
VirtualHost "localhost"
    authentication = "internal_hashed"
```

Restart Prosody:

```bash
sudo systemctl restart prosody
```

---

# Generate SSL Certificate

Generate a self-signed certificate:

```bash
sudo prosodyctl cert generate localhost
```

If necessary, copy the generated certificate and key into the Prosody certificates directory:

```bash
sudo cp /var/lib/prosody/localhost.crt /etc/prosody/certs/
sudo cp /var/lib/prosody/localhost.key /etc/prosody/certs/
```

Restart Prosody again:

```bash
sudo systemctl restart prosody
```

Verify certificates:

```bash
sudo prosodyctl check certs
```

---

# Register Agent Accounts

Create the XMPP accounts used by the system:

```bash
sudo prosodyctl register order localhost order123

sudo prosodyctl register inventory localhost inventory123

sudo prosodyctl register chef localhost chef123

sudo prosodyctl register delivery localhost delivery123
```

---

# Project Configuration

Update `config/settings.py`:

```python
XMPP_HOST = "127.0.0.1"
XMPP_PORT = 5222
XMPP_DOMAIN = "localhost"

ORDER_AGENT_JID = "order@localhost"
ORDER_AGENT_PASSWORD = "order123"

INVENTORY_AGENT_JID = "inventory@localhost"
INVENTORY_AGENT_PASSWORD = "inventory123"

CHEF_AGENT_JID = "chef@localhost"
CHEF_AGENT_PASSWORD = "chef123"

DELIVERY_AGENT_JID = "delivery@localhost"
DELIVERY_AGENT_PASSWORD = "delivery123"
```

---

# Verify the Connection

Run the test script:

```bash
python test_agents.py
```

Expected output:

```text
==================================================
OrderAgent connected
JID: order@localhost
==================================================
OrderAgent is ready.

==================================================
InventoryAgent connected
JID: inventory@localhost
==================================================
InventoryAgent is ready.

Agents started.
```

---

# Run the GUI

Launch the application:

```bash
python main.py
```

---

# Project Structure

```text
Restaurant-Multi-Agent-Order-Management-System/
│
├── agents/
├── config/
├── docs/
├── gui/
├── messaging/
├── services/
├── tests/
│
├── main.py
├── test_agents.py
├── requirements.txt
└── README.md
```

---

# Troubleshooting

### SPADE cannot connect

Check that Prosody is running:

```bash
sudo systemctl status prosody
```

Verify that port **5222** is listening:

```bash
sudo ss -tlnp | grep 5222
```

---

### Certificate errors

Verify certificates:

```bash
sudo prosodyctl check certs
```

Restart Prosody after any certificate changes:

```bash
sudo systemctl restart prosody
```

---

### Authentication errors

Ensure the XMPP accounts are registered:

```bash
sudo prosodyctl register order localhost order123
```

Verify that the JIDs and passwords in `config/settings.py` match the registered accounts.

---

# Current Development Status

- ✅ PySide6 GUI
- ✅ Prosody XMPP Server
- ✅ SPADE Integration
- ✅ OrderAgent
- ✅ InventoryAgent
- ✅ Agent Authentication
- ⏳ Agent-to-Agent Messaging
- ⏳ Complete Restaurant Workflow
- ⏳ GUI Integration