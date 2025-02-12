# Holiday-Management-Application

# 🎉 Holiday Management Application

This is a **Django application that fetches holiday data from the **Calendarific API** and allows users  to display holidays based on country and year.

---

## 📜 **Features**
✅ Fetches holiday data from Calendarific API  
✅ Allows users to filter holidays by **country, year, month, and day**  
✅ Caches API responses to reduce redundant API calls  
✅ Uses **Django REST Framework (DRF)** for the backend  

---

## ⚙️ **Technologies Used**
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite  
- **Caching:** Django’s caching framework  
- **API Used:** Calendarific API  

---

## 🚀 **Getting Started**
Follow these steps to set up and run the project on your local machine.

### 🔹 **1. Clone the Repository**
```sh
git clone https://github.com/your-username/Holiday-Management-Application.git
cd Holiday-Management-Application


🖥 Backend Setup (Django)
🔹 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

pip install -r requirements.txt


Set Up Environment Variables
Create a .env file in the backend directory and add:


CALENDARIFIC_API_KEY=your_api_key_here


Apply Migrations

python manage.py migrate


Run the Django Server

python manage.py runserver

Your backend API will now be available at:
http://127.0.0.1:8000/



ENDPOINT:"/api/holidays/?country=US&year=2024",
ENDPONT:"/api/holidays/?country=IN&year=2024&month=12"
ENDPOINT:"/api/holidays/?country=GB&year=2024&month=12&day=25"


