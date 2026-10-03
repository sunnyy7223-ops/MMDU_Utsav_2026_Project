# MMDU Utsav 2026 🎉

A college **Event Management System** developed for MMDU Utsav 2026.

The project provides a simple web-based platform where users can explore college events, view the schedule, register for events, and submit contact information.

## 🚀 Features

- Home page for MMDU Utsav 2026
- Events page
- Event schedule
- Online event registration
- SQLite database integration for registrations
- Registration records page
- Contact page
- Responsive and organized frontend
- Flask backend

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **SQLite**
- **HTML5**
- **CSS3**
- **Jinja2**

## 📁 Project Structure

```text
MMDU_Utsav_2026/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── events.html
    ├── schedule.html
    ├── registration.html
    ├── registrations.html
    └── contact.html
```

> The local SQLite database is intentionally excluded from GitHub using `.gitignore`. This prevents local registration data from being uploaded.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd MMDU_Utsav_2026
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python app.py
```

### 5. Open the website

Open the local address shown by Flask in your browser, usually:

```text
http://127.0.0.1:5000/
```

## 🗄️ Database

The project uses **SQLite** to store event registration information.

The database file is kept local and is not included in the public GitHub repository.

## 🎓 Project Purpose

This project was created as a college project to demonstrate basic web development, Flask backend development, form handling, and database integration.

## 👨‍💻 Author

**MMDU Utsav 2026 Project**

Built as a college Event Management System project.
