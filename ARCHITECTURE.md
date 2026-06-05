# NetOps Center Architecture

## Overview

NetOps Center is a Network Operations Platform designed for managing, monitoring and automating enterprise network infrastructure.

Supported platforms:

- Cisco IOS
- Cisco IOS-XE
- Cisco NX-OS

Future support:

- FortiGate
- MikroTik
- Juniper

---

# High-Level Architecture

```text
                +----------------+
                |    Frontend    |
                | React / NextJS |
                +--------+-------+
                         |
                         v
                +----------------+
                |   FastAPI API  |
                +--------+-------+
                         |
      +------------------+------------------+
      |                  |                  |
      v                  v                  v

+-----------+    +---------------+   +-------------+
| PostgreSQL|    | SSH Engine    |   | Scheduler   |
| Database  |    | Netmiko/Nornir|   | Background  |
+-----------+    +---------------+   +-------------+
```

---

# Core Components

## Frontend

Responsibilities:

- Dashboard
- Device Inventory
- Monitoring Views
- Reports
- Configuration Backup UI

Technology:

```text
React / NextJS
```

---

## Backend API

Responsibilities:

- Authentication
- Device Management
- Credential Management
- Monitoring API
- Automation API

Technology:

```text
FastAPI
```

---

## Database

Responsibilities:

- Inventory
- Credentials
- Monitoring History
- Job Results

Technology:

```text
PostgreSQL
```

---

## SSH Engine

Responsibilities:

- Device Discovery
- Command Execution
- Health Checks
- Configuration Backup

Technology:

```text
Netmiko
Nornir
Paramiko
```

---

# Data Model

## Site

Represents a physical location.

Examples:

- Tehran DC
- Shiraz POP
- Mashhad POP

---

## Credential Profile

Stores encrypted credentials.

Types:

- Username/Password
- SSH Key

---

## Device

Represents a network device.

Attributes:

- Hostname
- IP Address
- Platform
- Vendor
- Site
- Credential Profile

---

# Security

## Credential Storage

Passwords are never stored in plaintext.

Method:

```text
AES Encryption (Fernet)
```

---

## API Authentication

Planned:

```text
JWT Authentication
RBAC
```

Roles:

- Admin
- Operator
- ReadOnly

---

# Monitoring Engine

Planned checks:

- CPU
- Memory
- Temperature
- Fan Status
- Power Supply
- Interface Errors
- CRC Errors
- Logs

---

# Automation Engine

Planned capabilities:

- Command Execution
- Configuration Backup
- Compliance Checks
- Bulk Operations

---

# Future Features

## Configuration Archive

Versioned configuration backups.

## Alerting

Integrations:

- Email
- Telegram
- Slack

## Reporting

- Device Health Reports
- Capacity Reports
- Inventory Reports

---

# Development Roadmap

Phase 1

- Backend Foundation
- Database
- Inventory

Phase 2

- Credential Management
- SSH Engine

Phase 3

- Monitoring

Phase 4

- Automation

Phase 5

- Frontend Dashboard

Phase 6

- Reporting & Alerting
