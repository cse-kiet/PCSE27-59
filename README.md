# Diabetic Retinopathy Detection System

A comprehensive web application for detecting diabetic retinopathy from fundus images using AI-powered analysis. This system provides patient management, image upload, analysis results, and detailed reporting features.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

### 🏥 Core Functionality
- **Dashboard**: Real-time statistics, recent activity, and visual analytics
- **Patient Management**: Complete patient records with medical history
- **Image Upload**: Drag-and-drop fundus image upload with preview
- **AI Analysis**: Mock ML-based diabetic retinopathy detection
- **Results Reporting**: Detailed analysis results with recommendations
- **Responsive Design**: Mobile-first, works on all devices

### 📊 Analytics & Visualization
- Severity distribution charts
- Patient age demographics
- Confidence score tracking
- Progression analysis over time

### 🎨 UI/UX Features
- Light/Dark mode toggle
- Professional medical-grade interface
- Real-time form validation
- Progress indicators
- Interactive charts with Chart.js
- Print-ready reports

## Technology Stack

- **Backend**: Flask 3.0 (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5.3 with custom CSS
- **Charts**: Chart.js 4.4
- **Image Processing**: Pillow (PIL)
- **Icons**: Bootstrap Icons

## Project Structure

```
diabetic_retinopathy_app/
├── app.py                      # Main Flask application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Dashboard
│   ├── patients.html          # Patient list
│   ├── patient_detail.html    # Patient details
│   ├── upload.html            # Upload interface
│   └── results.html           # Analysis results
├── static/
│   ├── css/
│   │   ├── style.css          # Main styles
│   │   └── dashboard.css      # Dashboard styles
│   ├── js/
│   │   ├── script.js          # Main JavaScript
│   │   ├── charts.js          # Chart configurations
│   │   └── upload.js          # Upload functionality
│   └── uploads/               # Uploaded images directory
└── utils/
    ├── __init__.py
    ├── image_processor.py     # Image processing utilities
    └── helpers.py             # Helper functions
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Step 1: Clone or Download

```bash
# If using git
git clone <repository-url>
cd diabetic_retinopathy_app

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Required Directories

```bash
# Windows
mkdir static\uploads

# macOS/Linux
mkdir -p static/uploads
```

### Step 5: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 6: Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### 1. Dashboard
- View overall system statistics
- Monitor recent scan activity
- Check severity distribution
- Analyze patient demographics

### 2. Patient Management
- Click "Patients" in the navigation
- View all registered patients
- Use search and filters to find specific patients
- Click "Add New Patient" to register (demo mode)
- Click patient name or ID to view detailed profile

### 3. Upload Fundus Image
- Click "Upload Scan" in navigation
- Select a patient from the dropdown
- Drag and drop an image or click to browse
- Supported formats: JPG, PNG (max 10MB)
- Click "Analyze Image" to process

### 4. View Results
- After analysis, view detailed results
- Check severity level and confidence score
- Review clinical findings
- Read recommendations
- Print or download report

## Mock Data

The application includes sample data for demonstration:
- 4 sample patients with medical histories
- 2 sample scans with analysis results
- Mock ML analysis function (simulates AI processing)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard page |
| `/patients` | GET | Patient list |
| `/patient/<id>` | GET | Patient details |
| `/upload` | GET | Upload page |
| `/analyze` | POST | Analyze image |
| `/results/<scan_id>` | GET | Analysis results |
| `/api/patients` | GET | Get patients (JSON) |
| `/api/scan-history` | GET | Get scan history (JSON) |
| `/api/dashboard-stats` | GET | Get dashboard stats (JSON) |

## Configuration

Edit `config.py` to customize:
- Secret key (IMPORTANT for production!)
- Upload folder path
- File size limits
- Allowed file extensions
- Session timeout

## Security Features

- Secure filename handling with `werkzeug.utils.secure_filename`
- File type validation
- File size restrictions
- XSS protection via Flask
- CSRF protection ready (add Flask-WTF in production)

## Customization

### Colors and Theming
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* ... */
}
```

### Adding Real ML Model
Replace the `mock_ml_analysis()` function in `app.py` with actual model inference:

```python
def ml_analysis(image_path):
    # Load your trained model
    model = load_model('path/to/model')
    
    # Preprocess image
    img = preprocess_image(image_path)
    
    # Make prediction
    prediction = model.predict(img)
    
    # Return results
    return format_results(prediction)
```

## Production Deployment

### Important Steps:

1. **Change Secret Key**
   ```python
   app.config['SECRET_KEY'] = 'your-production-secret-key'
   ```

2. **Use Production Database**
   - Replace mock data with SQLite/PostgreSQL
   - Install Flask-SQLAlchemy
   - Create proper database models

3. **Enable HTTPS**
   - Use SSL certificates
   - Deploy behind nginx/Apache

4. **Environment Variables**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

5. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

### Upload Folder Permissions
```bash
# Windows
icacls static\uploads /grant Users:F

# macOS/Linux
chmod 755 static/uploads
```

### Module Not Found
```bash
# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

## Browser Compatibility

- Chrome/Edge: ✅ Fully supported
- Firefox: ✅ Fully supported
- Safari: ✅ Fully supported
- Mobile browsers: ✅ Responsive design

## Contributing

This is a demonstration project. For real medical use:
1. Implement actual ML model
2. Add proper database
3. Implement user authentication
4. Add data encryption
5. Comply with HIPAA/medical data regulations

## Medical Disclaimer

⚠️ **IMPORTANT**: This application is for demonstration purposes only. It should NOT be used for actual medical diagnosis. All AI predictions are simulated. Real medical decisions should be made by qualified healthcare professionals.

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- Check the documentation above
- Review the code comments
- Test with sample images
- Verify all dependencies are installed

## Acknowledgments

- Bootstrap team for the UI framework
- Chart.js for visualization library
- Flask community for excellent documentation
- Medical professionals for domain knowledge

## Version History

- **v1.0.0** (2024): Initial release
  - Core functionality
  - Mock ML analysis
  - Patient management
  - Responsive UI
  - Dashboard analytics

---

**Made with ❤️ for healthcare innovation**#   I n n o t e c h - 2 0 2 5 - P R J - 0 8 2  
 