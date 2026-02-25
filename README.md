# 🎓 AI Powered Student Management System

## 📌 Project Overview

The **AI Powered Student Management System** is a backend application built using **FastAPI** that manages student records and provides **smart search functionality** using AI-based filtering.

The system allows users to:

* Add student details
* Retrieve student information
* Perform intelligent search on student data
* Manage records efficiently

---

## 🧱 Project Structure

```
ai_powered_student_management/
│
├── main.py            # FastAPI application
├── requirements.txt   # Dependencies
├── README.md
```

---

## ⚙️ Technologies Used

* FastAPI
* Python
* Pydantic
* Uvicorn
* AI-based search logic

---

## 🚀 Features

✅ Add student records
✅ Fetch all students
✅ Smart AI search for students
✅ Validation using Pydantic
✅ Proper error handling using HTTPException
✅ REST API design

---

## 📡 API Endpoints

### ➤ Add Student

POST `/students`

Adds a new student record.

---

### ➤ Get All Students

GET `/students`

Returns list of all students.

---

### ➤ Smart Search Students

GET `/search?query=`

Uses AI-based logic to find matching students.

Returns:

* Count of matched students
* Matching student list

---

## ▶️ How to Run

### Install dependencies

```
pip install -r requirements.txt
```

### Start server

```
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing

APIs tested using:

* Swagger UI
* Postman

---

## 🎯 Learning Outcomes

* FastAPI backend development
* API validation using Pydantic
* Smart search implementation
* REST API design
* Error handling strategies

---

## 👩‍💻 Author

Student Project – AI Powered Student Management System
