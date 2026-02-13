🧊 Zimna Backend
Zimna is an AI-powered life planning and goal management platform designed to help users transform long-term ambitions into clear, actionable steps.

This repository houses the backend service, built with Django and Django REST Framework, providing the engine for authentication, goal management, and AI-driven task orchestration.

🚀 Features
Secure Auth: User authentication and authorization.

Goal Engine: Comprehensive goal creation and management.

Task Intelligence: Automated task generation and tracking.

Smart Scheduling: Logic-based planning and scheduling.

AI Integration: Goal breakdown powered by LLMs.

Analytics: Progress tracking and productivity insights (Planned).

🛠 Tech Stack
Language: Python

Framework: Django & Django REST Framework

Database: PostgreSQL (Planned)

Auth: JWT Authentication (Planned)

AI: OpenAI / LLM Integration (Planned)

📂 Project Structure
Plaintext

backend/
├── config/             # Django project settings
├── goals/              # Core goals & task application
├── venv/               # Virtual environment (Git ignored)
├── manage.py           # Django CLI
├── README.md           # Documentation
└── requirements.txt    # Project dependencies
⚙️ Local Development Setup (Windows)
Follow these steps to get your local environment up and running.

1. Navigate to the Directory
Bash

cd backend
2. Environment Setup
Create and activate your virtual environment:

PowerShell

# Create environment
python -m venv venv

# Activate environment
.\venv\Scripts\activate
Note: You should see (venv) appear in your terminal prefix.

3. Troubleshooting Execution Policy
If you encounter a "scripts disabled" error in PowerShell, run:

PowerShell

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Then repeat the activation step above.

4. Install & Run
Bash

# Install dependencies
pip install -r requirements.txt

# Start the development server
python manage.py runserver
📈 Roadmap
Phase 1: Core Backend (Current)
RESTful API for Goals & Tasks

User Authentication

Base Planner logic

Phase 2: Intelligence
AI-driven task breakdown

Context-aware smart rescheduling

Personalized productivity profiling

Phase 3: Scale
Team collaboration modules

Accountability & notification systems

Advanced Analytics dashboard

🤝 Contribution
This project is currently under active development. If you have feedback or find a bug, feel free to open an issue or reach out.

📄 License
This project is private and proprietary. All rights reserved.

✨ Author
Developed by Jesse Adesina as part of the Zimna AI platform.