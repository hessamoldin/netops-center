# NetOps Center

## Day 2 Progress Report

**Date:** 2026-06-11

---

# Completed Sprints

---

## Sprint 2 — Site CRUD API

Endpoints implemented:

```
POST   /sites
GET    /sites
GET    /sites/{id}
DELETE /sites/{id}
```

Fixes applied:

- Removed orphan directories from project root
- Fixed `site_id` type from `str` to `UUID` in router

---

## Sprint 3 — Credential Management

### Fernet Encryption

Passwords are encrypted before storage using AES (Fernet).

```
Plain Password  →  Fernet Encrypt  →  Database
```

Password is never returned in API responses.

### Endpoints implemented:

```
POST   /credentials
GET    /credentials
GET    /credentials/{id}
DELETE /credentials/{id}
```

### New files:

```
backend/app/core/security.py
backend/app/models/credential.py
backend/app/schemas/credential.py
backend/app/api/credentials.py
```

### Security:

```
FERNET_KEY stored in .env
.env added to .gitignore
password_encrypted stored in DB
password never exposed in API response
```

---

## Sprint 4 — Device Inventory

### Data Model:

```
Device
 ├── id              UUID
 ├── hostname        String
 ├── mgmt_ip         String
 ├── platform        String (ios / iosxe / nxos)
 ├── vendor          String
 ├── site_id         FK → sites
 ├── credential_id   FK → credential_profiles
 └── created_at      Timestamp
```

### Endpoints implemented:

```
POST   /devices
GET    /devices
GET    /devices/{id}
DELETE /devices/{id}
```

### Validations:

- site_id must exist
- credential_id must exist
- hostname must be unique
- mgmt_ip must be unique

### New files:

```
backend/app/models/device.py
backend/app/schemas/device.py
backend/app/api/devices.py
```

---

# Current Architecture

```
FastAPI
   │
   ├── /sites
   ├── /credentials
   └── /devices
         │
         ▼
   SQLAlchemy
         │
         ▼
   PostgreSQL
```

---

# Data Model Overview

```
Site
 └── Device
       ├── site_id         → Site
       └── credential_id   → CredentialProfile
```

---

# Database Migrations

```
d730722f3e4b  create sites table
265c5cd2de86  create credential_profiles table
9cbb9d237d49  create credential_profiles table v2
1331ea7cf501  create devices table
```

---

# Current Status

```
Git + GitHub SSH        ✅
Site CRUD API           ✅
Credential Encryption   ✅
Device Inventory        ✅
.env gitignore          ✅
```

---

# Roadmap

## Sprint 5

SSH Discovery Engine

- Connect to device via Netmiko
- Execute `show version`
- Auto-detect platform (ios / iosxe / nxos)

---

## Sprint 6

Health Check Engine

Checks:

- CPU
- Memory
- Temperature
- Fan Status
- Power Supply
- Interface Errors
- CRC
- Drops
- Logs
