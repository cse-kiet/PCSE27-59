"""
Helper utility functions for DR Detection System
"""

from datetime import datetime, timedelta
import hashlib
import re

def generate_unique_id(prefix=''):
    """Generate unique ID with timestamp"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return f"{prefix}{timestamp}"

def format_date(date_string, format='%Y-%m-%d'):
    """Format date string to specified format"""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime(format)
    except:
        return date_string

def calculate_age(birth_date):
    """Calculate age from birth date"""
    try:
        birth = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.now()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age
    except:
        return None

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    pattern = r'^[\d\s\-\+\(\)]{10,}$'
    cleaned = re.sub(r'\D', '', phone)
    return len(cleaned) >= 10

def hash_string(text):
    """Generate hash for string"""
    return hashlib.sha256(text.encode()).hexdigest()

def truncate_text(text, length=100):
    """Truncate text to specified length"""
    if len(text) <= length:
        return text
    return text[:length] + '...'

def get_severity_color(severity):
    """Get Bootstrap color class for severity level"""
    colors = {
        'None': 'success',
        'Mild': 'info',
        'Moderate': 'warning',
        'Severe': 'danger',
        'Proliferative': 'danger'
    }
    return colors.get(severity, 'secondary')

def get_risk_level(hba1c, blood_sugar):
    """Calculate risk level based on HbA1c and blood sugar"""
    if hba1c < 7 and blood_sugar < 140:
        return 'Low'
    elif hba1c < 8 and blood_sugar < 180:
        return 'Medium'
    else:
        return 'High'

def format_file_size(bytes):
    """Format bytes to human readable size"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} TB"

def sanitize_filename(filename):
    """Remove unsafe characters from filename"""
    return re.sub(r'[^\w\s.-]', '', filename)

def get_time_ago(date_string):
    """Get relative time string (e.g., '2 hours ago')"""
    try:
        date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        diff = now - date
        
        if diff.days > 365:
            return f"{diff.days // 365} year{'s' if diff.days // 365 > 1 else ''} ago"
        elif diff.days > 30:
            return f"{diff.days // 30} month{'s' if diff.days // 30 > 1 else ''} ago"
        elif diff.days > 0:
            return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
        elif diff.seconds > 3600:
            return f"{diff.seconds // 3600} hour{'s' if diff.seconds // 3600 > 1 else ''} ago"
        elif diff.seconds > 60:
            return f"{diff.seconds // 60} minute{'s' if diff.seconds // 60 > 1 else ''} ago"
        else:
            return "Just now"
    except:
        return date_string

def paginate_list(items, page=1, per_page=10):
    """Paginate a list of items"""
    start = (page - 1) * per_page
    end = start + per_page
    return {
        'items': items[start:end],
        'page': page,
        'per_page': per_page,
        'total': len(items),
        'pages': (len(items) + per_page - 1) // per_page
    }

def create_search_index(text):
    """Create searchable index from text"""
    return ' '.join(text.lower().split())

def filter_dict(d, keys):
    """Filter dictionary by keys"""
    return {k: v for k, v in d.items() if k in keys}