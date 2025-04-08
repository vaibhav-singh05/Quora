# ❓ Quora Clone (Django Based Q&A Web App)

This is a **Quora-style Question & Answer Website** built using **Django**. Users can:
- ✅ **Register/Login**
- ✅ **Post Questions**
- ✅ **Answer Questions**
- ✅ **Search Questions** by keywords
- ✅ **View Profiles** and update profile pictures

---

## 🚀 GitHub Link
The source code is hosted at: [https://github.com/vaibhav-singh05/quora](https://github.com/vaibhav-singh05/quora)

---

## 🛠 **Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone <your_repo_url>
cd quora
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
```
- **Activate it:**
  - **Windows:** `venv\Scripts\activate`
  - **Mac/Linux:** `source venv/bin/activate`

### **3️⃣ Install Requirements**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser (optional)**
```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔍 **Features**
- User Authentication (Register/Login/Logout)
- Post Questions
- Answer Questions
- Search Functionality
- Profile Page with Profile Picture Upload
- Fully Responsive UI with Bootstrap

---

## 🧩 **Project Structure**
```
quora/
├── core/                      # Main App
│   ├── admin.py
│   ├── models.py              # Question, Answer, Profile Models
│   ├── views.py               # Views for Q&A, Profile, Search
│   ├── urls.py
│   └── ...
│
├── quora/                     # Project Config
│   ├── settings.py            # Django Settings
│   ├── urls.py                # Root URLs
│   └── ...
│
├── media/profile_pic/        # Uploaded Profile Pictures
├── static/img/               # Static Images
├── templates/                # HTML Templates
│   ├── base.html
│   ├── index.html
│   ├── question_detail.html
│   └── ...
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 👤 **Author**
- **Name:** Vaibhav Singh
- **Email:** [vaibhavsingh273010@gmail.com](mailto:vaibhavsingh273010@gmail.com)
- **LinkedIn:** [https://www.linkedin.com/in/vaibhav-singh-2a5991229/](https://www.linkedin.com/in/vaibhav-singh-2a5991229/)

---

### 🎉 Happy Learning & Building! 🚀

