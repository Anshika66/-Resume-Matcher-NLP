# 🔍 Resume Matcher using NLP & Flask

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web-green)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-orange)
![Machine Learning](https://img.shields.io/badge/ML-Cosine%20Similarity-purple)
![Status](https://img.shields.io/badge/Project-Complete-success)

---

## 🚀 Overview
**Resume Matcher** is an intelligent web-based application that evaluates how well a resume matches a given job description using **Natural Language Processing (NLP)** and **Machine Learning** techniques.

It helps **job seekers** understand resume relevance before applying and assists **recruiters** in shortlisting the most suitable candidates quickly and objectively.

---

## 🎯 Problem Statement
Job applicants often apply to roles without knowing how closely their resume aligns with job requirements.  
Manual resume screening is **time-consuming, subjective, and inefficient**.

### ✅ Solution
An automated NLP-based system that compares resumes with job descriptions and generates **similarity scores** to measure relevance and rank candidates accordingly.

---

## 💡 Key Features
- 📄 Upload multiple resumes at once  
- 📝 Paste any job description  
- 📊 Resume ranking using similarity scores  
- 🧠 NLP-based text comparison  
- 📂 Supports **PDF, DOCX, and TXT** formats  
- 🎨 Clean, modern, and responsive UI  
- ⚡ Fast and accurate matching  

---

## 🛠️ Tech Stack

### 🔧 Backend
- Python  
- Flask  
- Scikit-learn  
- PyPDF2  
- docx2txt  

### 🎨 Frontend
- HTML  
- CSS  
- Bootstrap  

### 🧠 NLP & Machine Learning
- TF-IDF Vectorization  
- Cosine Similarity  

---

## 🧠 How It Works
1. User enters a job description  
2. Uploads one or more resumes  
3. Text is extracted from each resume  
4. Text data is vectorized using **TF-IDF**  
5. **Cosine similarity** measures relevance  
6. Top matching resumes are displayed with scores  

---

## 📐 System Architecture

Job Description  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity  
↓  
Resume Ranking

---
## 📁 Project Structure

```bash
Resume Matcher/
│
├── input resumes/          # Sample resumes
├── uploads/                # Uploaded resumes
├── templates/
│   └── matchresume.html    # Frontend template
│
├── main.py                 # Flask backend
├── README.md               # Documentation

```

---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository

    git clone https://github.com/your-username/resume-matcher.git
    cd resume-matcher

2️⃣ Install Required Libraries

    pip install flask scikit-learn PyPDF2 docx2txt

3️⃣ Run the Application
    
    python main.py

4️⃣ Open in Browser

    http://127.0.0.1:5000/

### 📊 Sample Output


- Displays **Top 3 matching resumes**
- Shows **similarity percentage**
- Helps users instantly assess resume relevance

### 🔮 Future Enhancements

- Skill extraction & keyword highlighting

- ATS-style resume scoring

- User authentication

- Cloud deployment (AWS / Render / Heroku)

- Resume improvement suggestions based on job description

### 🎓 Learning Outcomes

✨ This project demonstrates practical application of NLP in real-world hiring and resume screening systems.

This project helped me gain hands-on experience in:

- NLP text preprocessing

- Machine learning similarity algorithms

- Flask backend development

- File handling and text extraction

- Frontend-backend integration

### 👩‍💻 Author

Anshika Srivastav
Computer Science Student

Skills:
Python | NLP | Flask | Machine Learning

📌 Open to internships and opportunities
