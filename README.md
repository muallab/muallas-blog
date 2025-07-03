# Mualla’s Blog

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/) [![Django 4.2](https://img.shields.io/badge/django-4.2-44b78b)](https://www.djangoproject.com/) \[![License: MIT](https://img.shields.io/badge/license-MIT-green)]

> **A clean, responsive Django blog platform with full content management.**

---

## 📖 Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Database Migrations](#database-migrations)
   * [Superuser Setup](#superuser-setup)
   * [Running the Server](#running-the-server)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

---

## ✨ Features

* **Static Pages:** Home and About templates
* **Article Management:** Create, Read, Update, Delete via Django ORM
* **Admin Panel:** Secure interface for managing posts
* **Responsive Design:** Bootswatch Cosmo theme + Google Fonts (Roboto)
* **Custom Styles:** Enhanced UI transitions and effects

---

## 🛠 Tech Stack

* **Backend:** Python 3.9+, Django 4.2
* **Database:** SQLite (default; adaptable to PostgreSQL, MySQL, etc.)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Bootswatch Cosmo), Google Fonts
* **Development:** Git, GitHub, VS Code, Git Bash / PowerShell

---

## ⚙️ Getting Started

Follow these steps to run the project locally.

### ✅ Prerequisites

* Python 3.9 or higher
* Git installed on your system

### 🚀 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/MuallasBlogProject.git
   cd MuallasBlogProject
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # macOS/Linux or Git Bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### 🗄 Database Migrations

```bash
python manage.py migrate
```

### 👤 Superuser Setup

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### ▶️ Running the Server

```bash
python manage.py runserver
```

Open your browser to `http://127.0.0.1:8000/`.

---

## 🧭 Usage

| Path                     | Description          |
| ------------------------ | -------------------- |
| `/`                      | Home page            |
| `/about/`                | About page           |
| `/articles/`             | List all articles    |
| `/articles/new/`         | Create a new article |
| `/articles/<id>/`        | View article detail  |
| `/articles/<id>/edit/`   | Edit an article      |
| `/articles/<id>/delete/` | Delete an article    |
| `/admin/`                | Admin dashboard      |

---

## 🗂 Project Structure

```
MuallasBlogProject/
├── blog/                  # Django app: models, views, forms, templates
├── MuallasBlogProject/    # Settings and URL configurations
├── templates/             # Global templates (base.html, includes)
├── static/                # Static assets: CSS, JS, images
├── venv/                  # Virtual environment (ignored by Git)
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository.
2. **Branch:** `git checkout -b feature/YourFeature`
3. **Commit:** `git commit -m "Add YourFeature"`
4. **Push:** `git push origin feature/YourFeature`
5. **Pull Request:** Open a PR and describe your changes.

Ensure your code adheres to [PEP 8](https://peps.python.org/pep-0008/) style guidelines.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
