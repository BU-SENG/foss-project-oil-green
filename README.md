# Campus Resource Hub

A centralized platform for students to access campus resources, book facilities, manage academic-related tasks, and receive quick support.

---

## 📘 Project Summary / Requirements

The **Campus Resource Hub** is designed to help university students easily access campus services and manage essential resources.

### **Key Requirements**

* Secure authentication (BU Student Email Only – `@student.babcock.edu.ng`)
* Dashboard for resource overview
* Facility booking system (labs, rooms, equipment, etc.)
* Contact/support channel for campus units
* Career hub for job and internship opportunities
* Student profile management
* Persistent login using encrypted cookies
* Admin-ready database structure
* Mobile-responsive UI
* Light transitions and custom UI components

---

## 🎯 Purpose / Objective

The Campus Resource Hub simplifies student access to important university services. It ensures that students can:

* Find and reserve campus resources quickly
* Communicate with campus departments
* Track bookings and personal information
* Access career opportunities easily

---

## 🚀 Key Features

* **Resource Directory**
  View available campus facilities with descriptions.

* **Booking System**
  Reserve labs, equipment, or study spaces.

* **Contact Centre**
  Reach campus departments (IT unit, halls, library, etc.)

* **Career Hub**
  Access internships, job posts, and career guidance.

* **Profile Page**
  Manage student details, hall info, guardian contact, and avatar.

* **Encrypted Cookie Login**
  Auto-login system using `EncryptedCookieManager`.

* **Custom Sidebar & Navbar**
  Replaces Streamlit’s default navigation.

* **Database Auto-Initialization**
  Tables for booking, resources, and contacts are created automatically.

---

## ⚙️ Tech Stack

| Layer                | Tools                                       |
| -------------------- | ------------------------------------------- |
| **Frontend**         | Streamlit (Custom UI, CSS animations)       |
| **Backend**          | Python                                      |
| **Database**         | SQLite                                      |
| **Authentication**   | Custom auth service + encrypted cookies     |
| **Utilities**        | Validators, session handler, date formatter |
| **Deployment Ready** | Streamlit Cloud / local server              |

---

## 📁 Project Structure

```
app_pages/
├── dashboard/
├── resources/
├── booking/
├── contacts/
├── careerhub/
└── profile/

components/
├── sidebar.py
├── navbar.py
└── cards/

services/
├── auth_service.py
├── booking_service.py
├── resource_service.py
└── contact_service.py

utils/
├── validators.py
├── session_state.py
├── constants.py
└── format_date.py

core/
└── app.py

assets/
├── css/
└── images/
```

---

## 🧪 Quick Start

### 🔸 **1. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

### 🔸 **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### 🔸 **3. Run Streamlit App**

```bash
streamlit run main.py
```

---

## 🔐 Environment Setup

Create a `.env` file in the root (optional for secret keys):

```
SECRET_KEY=your_secret_key_here
```

You can also adjust:

* Database path
* Admin account credentials
* Cookie password

---

## 💻 Scripts (Python)

```
pip install -r requirements.txt      # Install dependencies
streamlit run main.py                # Development server
python -m pytest                     # Run tests (if added)
```

---

## 🤝 How to Contribute / Contact

Contributions, feature requests, and bug reports are welcome.

* Submit issues on GitHub
* Create a PR for enhancements
* Contact project maintainers (email or GitHub username)

---

## ⭐ Summary

The **Campus Resource Hub** serves as a complete student support platform, integrating booking, resources, contacts, profiles, and career services into one clean and modern interface.
