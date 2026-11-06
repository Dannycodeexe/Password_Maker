# Password_Maker

## 3-2-1 Password Forge

A secure, full-stack web application that generates memorable, high-entropy passphrases using a custom user-defined word bank, paired with an interactive server-validated memory game. 

## What This Project has
- **Cryptographic Security:** Utilizes Python's built-in `secrets` module instead of the standard `random` library for true pseudo-randomness.
- **RESTful API Architecture:** Exposes dedicated Flask endpoints (`/api/generate` and `/api/game/validate`) handling JSON data exchange and backend validation.
- **Server-Side State Validation:** Implements strict anti-cheat and state tracking on the backend for the memory challenge game, ensuring clients cannot bypass rules.
- **Modern, Accessible UI:** Features a custom cool-color glassmorphism aesthetic, full keyboard accessibility (`aria-label` standards, Enter-key listeners, and auto-refocusing workflow), and a seamless soft-reset state loop.

## Prerequisites & Installation
Ensure you have Python installed, then install the required dependency:

```bash
pip install flask
