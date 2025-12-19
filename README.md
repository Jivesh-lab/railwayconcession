# 📘 Railway Concession — Student Online Application System

A **web application** to simplify the process of applying for *railway student concessions*. Instead of filling physical forms manually, this system lets students submit details online and get their concession processed quickly.

---

## 🧠 🚆 Project Overview

The Railway Concession system provides:

- ✔ Easy online form submission  
- ✔ Student data validation  
- ✔ Django-based backend processing  
- ✔ Static responsive frontend  
- ✔ Saves data locally (SQLite)

---

## 🛠️ Technology Stack

| Layer         | Technology                 |
|---------------|----------------------------|
| Frontend      | HTML, CSS, JavaScript      |
| Backend       | Python (Django)            |
| Database      | SQLite (default Django DB) |
| Templating    | Django Templating Engine   |
| Static Assets | CSS, Images                |
| Deployment    | GitHub / Local Server      |

---

## 🏛️ Architecture Diagram

```mermaid
flowchart TD
    A[User Browser] -->|HTTP Request| B[Django Views]
    B --> C[Form Validation]
    C --> D[Database (SQLite)]
    D --> E[Rendered HTML Response]
    E --> A
    B --> Static[CSS / JS / Images]
    Static --> A 

````

💻 Setup & Installation (Local)

Follow these step-by-step instructions to run this project locally.

1️⃣ Clone the repository
git clone https://github.com/Jivesh-lab/railwayconcession.git
cd railwayconcession

2️⃣ Create & activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install django


(If a requirements.txt exists, use:)

pip install -r requirements.txt

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the development server
python manage.py runserver

6️⃣ Open in browser
http://127.0.0.1:8000/

