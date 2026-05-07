# 🩺 Diabetic Retinopathy Detection System

AI-powered web application for detecting diabetic retinopathy from retinal fundus images using deep learning-based analysis.

Built with Flask, Bootstrap, and modern healthcare-focused UI design.

---

## ✨ Features

### 🏥 Core Features
- Patient management system
- Fundus image upload with preview
- AI-based diabetic retinopathy analysis
- Detailed diagnostic reports
- Dashboard with analytics
- Responsive medical-grade UI

### 📊 Analytics
- Severity distribution charts
- Confidence score tracking
- Patient demographics
- Historical scan analysis

### 🎨 UI/UX
- Dark/Light mode
- Drag-and-drop upload
- Interactive charts
- Print-ready reports
- Mobile responsive design

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|------|
| Python 3.8+ | Backend |
| Flask 3.0 | Web Framework |
| Bootstrap 5.3 | UI Framework |
| Chart.js | Data Visualization |
| Pillow (PIL) | Image Processing |
| JavaScript ES6+ | Frontend Logic |

---

## 📁 Project Structure

```bash
diabetic_retinopathy_app/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── patients.html
│   ├── patient_detail.html
│   ├── upload.html
│   └── results.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
└── utils/
    ├── image_processor.py
    └── helpers.py
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd diabetic_retinopathy_app
```

### 2️⃣ Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

Open in browser:

```bash
http://localhost:5000
```

---

## 📸 Application Modules

### 🏠 Dashboard
- Real-time statistics
- Recent activity tracking
- Severity analytics

### 👨‍⚕️ Patient Management
- Patient records
- Medical history
- Search & filtering

### 📤 Image Upload
- Drag-and-drop support
- Image preview
- JPG/PNG support

### 🤖 AI Analysis
- Retinopathy severity detection
- Confidence score generation
- Clinical recommendations

### 📄 Reports
- Detailed analysis report
- Printable format
- Scan history tracking

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard |
| `/patients` | GET | Patient list |
| `/patient/<id>` | GET | Patient details |
| `/upload` | GET | Upload page |
| `/analyze` | POST | Analyze image |
| `/results/<scan_id>` | GET | Analysis results |

---

## 🔒 Security Features

- Secure file upload handling
- File type validation
- Upload size restriction
- XSS protection
- CSRF-ready architecture

---

## 🧠 Adding Real ML Model

Replace the mock analysis function with actual model inference:

```python
def ml_analysis(image_path):

    model = load_model("model_path")

    img = preprocess_image(image_path)

    prediction = model.predict(img)

    return format_results(prediction)
```

---

## 🚀 Production Deployment

### Important Steps

- Change Flask secret key
- Use PostgreSQL/MySQL
- Enable HTTPS
- Store secrets in environment variables
- Deploy with Gunicorn + Nginx

### Production Server

```bash
pip install gunicorn

gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## ⚠️ Medical Disclaimer

This project is for educational and demonstration purposes only.

It must NOT be used for real medical diagnosis or treatment decisions without professional medical validation.

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

Fork the repository and submit a pull request.

---

## 📜 License

MIT License

---

## ❤️ Acknowledgements

- Flask Community
- Bootstrap Team
- Chart.js
- Healthcare AI Research Community

---

## 📌 Version

### v1.0.0
- Initial release
- Mock AI analysis
- Patient management
- Dashboard analytics
- Responsive UI
