# AI Recruiter - CV Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Project Overview

**AI Recruiter** is an intelligent CV/Resume analyzer tool that automatically extracts key information from candidate descriptions. It identifies and categorizes:

- **Skills** - Soft and technical skills
- **Technologies** - Frameworks, tools, and platforms
- **Programming Languages** - Languages used by the candidate

The extracted information is displayed in an intuitive web interface (built with Streamlit) and provided as structured JSON output for easy integration with recruitment systems.

---

## 🎯 Problem Statement

Recruiters spend significant time manually reading and analyzing CVs to identify candidate qualifications. This tool streamlines the process by automatically extracting relevant information.

**Example:**
> "I worked on machine learning projects using Python and TensorFlow and built CNN models."

Instead of manually parsing this text, AI Recruiter automatically extracts:
- **Technologies**: CNN, TensorFlow
- **Languages**: Python
- **Skills**: Machine Learning, Computer Vision

---

## ✨ Features

- ✅ Accepts CV/resume text input
- ✅ Extracts skills, technologies, and programming languages
- ✅ Handles common abbreviations (AI, ML, NLP, etc.)
- ✅ Infers related skills from technologies
- ✅ Provides structured JSON output
- ✅ User-friendly web interface with Streamlit
- ✅ Real-time text processing

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core programming language |
| **Streamlit** | Web interface and frontend |
| **JSON** | Data serialization and output format |
| **Rule-based NLP** | Text processing and keyword extraction |

---

## 📊 Methodology

The system follows a **Rule-based NLP approach** with the following pipeline:

### 1. **Input Processing**
User inputs a CV or resume text containing candidate qualifications.

### 2. **Text Normalization**
- Converts input to lowercase for consistent matching
- Handles different casing variations (Python, PYTHON, python)

### 3. **Keyword Extraction**
- Matches text against predefined lists of:
  - Skills
  - Technologies
  - Programming Languages

### 4. **Abbreviation Expansion**
- Converts common abbreviations to full forms:
  - `ML` → Machine Learning
  - `AI` → Artificial Intelligence
  - `NLP` → Natural Language Processing

### 5. **Skill Inference**
- Associates technologies with related skills
- **Examples:**
  - CNN → Computer Vision
  - TensorFlow → Machine Learning
  - Pandas → Data Analysis
  - OpenCV → Computer Vision

### 6. **JSON Generation**
- Compiles extracted information into structured JSON format
- Ready for API integration or display

---

## 📈 Results

The system successfully extracts relevant information from conversational candidate descriptions.

### Example Input:
```
"I built an image classification project using CNN and TensorFlow. 
I used Python and Pandas to analyze the dataset."
```

### Example Output:
```json
{
    "skills": [
        "computer vision",
        "machine learning",
        "data analysis"
    ],
    "technologies": [
        "cnn",
        "tensorflow",
        "pandas"
    ],
    "languages": [
        "python"
    ]
}
```

---

## 📸 Screenshots

### Main Interface
![AI Recruiter Main Interface](Screenshot%202026-08-21%20185409.png)

### Results Display
![AI Recruiter Results](Screenshot%202026-08-21%20185416.png)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/itsmeYUVRAJ6629/AI-Recruiter.git
   cd AI-Recruiter
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Web Interface**
   - Open your browser and navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
AI-Recruiter/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── data/
    ├── skills.txt        # Predefined skills list
    ├── technologies.txt  # Predefined technologies list
    └── languages.txt     # Predefined programming languages list
```

---

## 🤔 Challenges Faced

- Building the Streamlit web interface (leveraged AI for this component)
- Understanding frontend frameworks for the first time
- Structuring the data extraction pipeline efficiently

---

## 🔮 Future Improvements

1. **Enhanced Dataset** - Expand from predefined lists to a comprehensive database of skills and technologies
2. **Resume File Upload** - Support PDF and document file uploads
3. **Candidate Matching** - Match candidates with job descriptions
4. **Additional Extraction** - Extract personal information (name, age, education, contact details)
5. **Multilingual Support** - Support multiple languages
6. **API Integration** - REST API for third-party integrations
7. **Machine Learning** - Replace rule-based approach with ML models for better accuracy
8. **Batch Processing** - Process multiple resumes in bulk

---

## 📝 Example Usage

### Using the Web Interface
1. Open the Streamlit application
2. Paste or type candidate information
3. Click "Extract Information"
4. View extracted skills, technologies, and languages
5. Download JSON output if needed

### Sample Inputs
```
"Senior Python developer with 5 years of experience in Django and Flask. 
Proficient in AWS, Docker, and Kubernetes. Machine learning enthusiast."
```

```
"Full-stack developer specializing in React, Node.js, and MongoDB. 
Experience with DevOps and CI/CD pipelines using GitHub Actions."
```

---


## 📋 Requirements

Create a `requirements.txt` file with:
```
streamlit>=1.0.0
```

---

## 👨‍💻 Author

**YUVRAJ** - AI Recruiter Developer

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Steps to Contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ❓ FAQ

**Q: What file formats are supported?**
A: Currently, the tool accepts text input. PDF and document support is planned for future releases.

**Q: Can I use this for production?**
A: Yes, but consider expanding the keyword lists and implementing the planned ML-based approach for better accuracy.

**Q: How accurate is the extraction?**
A: The rule-based approach works well for common skills and technologies. Accuracy improves with a larger keyword database.

---

## 📧 Support

For questions or issues, please open a GitHub issue or contact the author.

---

**Happy Recruiting! 🎉**
