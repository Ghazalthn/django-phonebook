# Django Phonebook Application

## 📋 Overview
The **Django Phonebook Application** is a web-based project that allows users to manage their private phonebooks. Each user has their own account where they can:
- Add, edit, view, and delete contacts.
- Search for specific contacts.
- Enjoy a user-friendly interface with secure authentication.

The application is built using Django, Bootstrap for styling, and supports Docker for easy deployment.

---

## 🚀 Features
- **Multi-User Support**: Each user has their own private phonebook.
- **CRUD Operations**: Create, Read, Update, and Delete contacts seamlessly.
- **Authentication System**: Login and logout securely.
- **Search Functionality**: Find contacts quickly by name.
- **Responsive Design**: Built with Bootstrap for a modern look.

---

## 📦 Prerequisites
- Python 3.10 or later
- Docker (optional, for easy setup)
- Git (to clone the repository)

---

## ⚙️ Installation and Setup

### **Manual Setup**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ghazalthn/django-phonebook.git
   cd django-phonebook
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver 8002
   ```

7. **Access the App**:
   - Open your browser and go to: [http://127.0.0.1:8002](http://127.0.0.1:8002)

---

### **Docker Setup (Recommended)**
1. **Ensure Docker is Installed**:
   - [Download Docker](https://www.docker.com/)

2. **Build and Run the Container**:
   ```bash
   docker-compose up --build
   ```

3. **Access the App**:
   - Open your browser and go to: [http://127.0.0.1:8002](http://127.0.0.1:8002)

---

## 💻 Usage
1. **Admin Access**:
   - Log in to the admin panel: [http://127.0.0.1:8002/admin/](http://127.0.0.1:8002/admin/)
   - Manage users, contacts, and more.

2. **User Features**:
   - Register a new account or log in.
   - Add, edit, and delete contacts.
   - Use the search bar to quickly find a contact.

---

## 🐳 Automating Deployment with Docker
The project includes a `Dockerfile` and `docker-compose.yml` for easy deployment.

### **How Docker Works for This Project**:
- The `Dockerfile` sets up a Python environment and installs the app's dependencies.
- The `docker-compose.yml` orchestrates the container, exposing the app on port `8002`.

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it.

---