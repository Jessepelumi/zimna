# Zimna Backend

Zimna is an AI-powered life planning and goal management platform designed to help users turn long-term goals into clear, actionable steps.

This repository contains the backend service for Zimna, built with Django and Django REST Framework. It provides REST APIs for authentication, goal management, task planning, scheduling, and AI-powered features.

---

## 🚀 Features

- User authentication and authorization
- Goal creation and management
- Task generation and tracking
- Smart planning and scheduling
- AI-powered goal breakdown
- Progress tracking and analytics (planned)

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (planned)
- PostgreSQL (planned)
- OpenAI / LLM Integration (planned)

---

## 📂 Project Structure
backend/
│
├── config/ # Django project settings
├── goals/ # Goals application
├── venv/ # Virtual environment (ignored in Git)
├── manage.py
├── README.md
└── requirements.txt

---

## ⚙️ Local Development Setup (Windows)

Follow the steps below to set up the backend locally.

---

#### 1. Navigate to Backend Directory
```bash
cd backend

#### 2. Create Virtual Environment (Windows Powershell)

```bash
python -m venv venv

#### 3. Activate Virtual Environment

```bash
venv\Scripts\activate

-> You should see (venv) in your terminal.

#### 4. Fix Execution Error (Windows only)

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

-> Then reactivate by repeating step 3.

#### 5. Install Dependencies

```bash
pip install -r requirements.txt

-> This installs Django and all required packages.

#### 6. Start Deployment Server

```bash
python manage.py runserver

---

## 📈 Roadmap

#### Phase 1 — Core Backend (Current)

- Authentication
- Goals API
- Task management
- Basic planner

#### Phase 2 — Intelligence

- AI task breakdown
- Smart rescheduling
- Productivity profiling

#### Phase 3 — Platform

- Team collaboration
- Accountability features
- Analytics dashboard

---

## 🤝 Contribution

This project is currently under active development. Feedback, issues, and suggestions are welcome.

---

## 📄 License

This project is private and proprietary. All rights reserved.

---

## ✨ Author

Built by Jesse Adesina as part of Zimna AI platform.
