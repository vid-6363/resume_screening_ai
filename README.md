AI Resume Screening System

An AI-powered web application that automates resume screening by matching resumes with job descriptions using Natural Language Processing (NLP).

🚀 Project Overview

This project helps recruiters and HR teams quickly evaluate resumes by calculating a **match percentage** between a candidate’s resume and a given job description. It reduces manual effort and speeds up the shortlisting process.

✨ Features

- Upload resume in *PDF format*
- Paste job description text
- Extracts resume content automatically
- Calculates **resume–job match score (%)**
- Simple and user-friendly web interface
- 
 🛠️ Tech Stack

- *Python*
- *Flask* – Web framework
- *PyPDF2* – Resume text extraction
- *Scikit-learn* – TF-IDF & Cosine Similarity
- *HTML* – Frontend template

 📂 Project Structure

resume_screening_ai/
│
├── app.py
├── resume_parser.py
├── similarity.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
└── index.html

