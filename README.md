# 🍽 Restaurant Multi-Agent Order Management System

A desktop-based Multi-Agent System (MAS) developed with **Python**, **SPADE**, and **PySide6**.

This project simulates a restaurant order workflow where multiple intelligent agents collaborate to process customer orders.

---

## Technologies

- Python 3.12+
- SPADE
- PySide6 (Qt)
- XMPP (Prosody)
- Git

---

## Project Architecture

```
Customer
    │
    ▼
PySide6 GUI
    │
    ▼
Order Agent
    │
    ▼
Inventory Agent
    │
    ▼
Chef Agent
    │
    ▼
Delivery Agent
```

Each agent has an independent responsibility and communicates through SPADE messages over an XMPP server.

---

## Agents

### Order Agent

- Receives customer orders
- Creates order IDs
- Starts the workflow

### Inventory Agent

- Checks ingredient availability
- Reserves inventory
- Sends inventory status

### Chef Agent

- Simulates food preparation
- Calculates cooking time
- Marks orders as ready

### Delivery Agent

- Assigns a delivery driver
- Estimates delivery time
- Completes the order

---

## Project Structure

```
restaurant-mas/

├── agents/
├── config/
├── data/
├── gui/
├── messaging/
├── models/
├── services/
├── tests/

├── main.py
├── requirements.txt
└── README.md
```

---

## Current Progress

- [x] Project setup
- [x] Desktop GUI
- [ ] SPADE infrastructure
- [ ] Order Agent
- [ ] Inventory Agent
- [ ] Chef Agent
- [ ] Delivery Agent
- [ ] GUI Integration
- [ ] Testing
- [ ] Documentation

---

## Screenshots

Coming soon.

---

## Author

Amirali Mhdypr