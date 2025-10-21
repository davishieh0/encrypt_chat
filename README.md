<div align="center">

# 🔐 Encrypt Chat

**Secure encrypted messaging system with user authentication**

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)
![Encryption](https://img.shields.io/badge/Encryption-Fernet%20(AES)-red.svg)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Functions](#-api-functions)
- [Project Structure](#-project-structure)
- [Development Checklist](#-development-checklist)

---

## 🎯 Overview

Encrypt Chat is a command-line encrypted messaging system that ensures secure communication between users. All messages are encrypted using **Fernet (AES)** encryption, and user passwords are hashed with **bcrypt** for maximum security.

---

## ✨ Features

- 🔒 **End-to-end encryption** using Fernet (AES-128)
- 🔑 **Secure authentication** with bcrypt password hashing
- 💾 **MongoDB storage** for users and encrypted messages
- 🚀 **Lightweight** command-line interface
- ⚡ **Fast** dependency management with uv

---

## 🛠️ Installation

### Prerequisites

- ![Python](https://img.shields.io/badge/-Python%203.13+-3776AB?logo=python&logoColor=white) Python 3.13 or higher
- ![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?logo=mongodb&logoColor=white) MongoDB (Atlas or local instance)
- ![uv](https://img.shields.io/badge/-uv-000000?logo=astral&logoColor=white) uv package manager

### 📦 Installing uv on Ubuntu

```bash
# Install uv using the official installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart your shell or source the config
source $HOME/.cargo/env

# Verify installation
uv --version
```

### ⚙️ Project Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd encrypt_chat

# Install dependencies
uv sync

# Configure environment variables
cp .env.example .env
# Edit .env with your MongoDB credentials
```

**`.env` configuration:**
```env
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority
MONGODB_DATABASE=your_database_name
```

---

## 🚀 Usage

### Register a New User

```bash
python3 encryptChat/main.py /register
```

### Send an Encrypted Message

```bash
python3 encryptChat/main.py /send
```

**Example workflow:**
```
$ python3 encryptChat/main.py /send
Username: alice
Password: ********
Authenticating...
Login successful!
Type your message: Hello, this is a secret message!
Username to send message: bob
Encrypting and sending message...
Message sent successfully!
```

---

## 📚 API Functions

### 🔐 Authentication

| Function | Description |
|----------|-------------|
| `register(username, password)` | Creates new user with bcrypt-hashed password |
| `login(username, password)` | Validates user credentials against database |

### 💬 Messages

| Function | Description |
|----------|-------------|
| `sendMessage(sender, receiver, message)` | Encrypts and sends message using Fernet |

### 🔑 Cryptography

| Function | Description |
|----------|-------------|
| `Crypto.encrypt(message)` | Encrypts plaintext message |
| `Crypto.decrypt(encrypted_message)` | Decrypts encrypted message |
| `Crypto.get_key()` | Returns the encryption key |

### 💾 Database

| Function | Description |
|----------|-------------|
| `createUser(data)` | Inserts new user into MongoDB |
| `getUser(field, value)` | Retrieves user by specified field |
| `createMessage(data)` | Saves encrypted message to database |

---

## 📁 Project Structure

```
encrypt_chat/
├── 📂 encryptChat/
│   ├── 🐍 main.py              # Application entry point
│   ├── 🔐 auth.py              # Authentication (login/register)
│   ├── 📂 db/
│   │   ├── __init__.py
│   │   └── 🗄️ mongoClient.py   # MongoDB client
│   ├── 📂 functions/
│   │   └── 📨 sendMessage.py   # Message sending logic
│   ├── 📂 models/
│   │   ├── __init__.py
│   │   ├── 👤 user.py          # User model
│   │   └── 💬 message.py       # Message model
│   └── 📂 utils/
│       ├── ⚙️ constants.py     # Environment variables
│       └── 📂 criptography/
│           └── 🔒 criptography.py  # Crypto class (Fernet)
├── 📄 pyproject.toml           # Project dependencies
├── 🔧 .env.example             # Environment template
└── 📖 README.md
```

---

## ✅ Development Checklist

### 🔒 Security

- [x] Passwords hashed with bcrypt
- [x] Messages encrypted with Fernet (AES)
- [x] Sensitive variables in `.env`
- [ ] Persistent encryption key management
- [ ] Input data validation

### 🎯 Features

- [x] User registration
- [x] User login
- [x] Encrypted message sending
- [ ] Message reading/listing
- [ ] Decryption of received messages
- [ ] Message status system (read/unread)


### 🏗️ Infrastructure

- [x] MongoDB connection
- [x] Dependency management (uv)

---
