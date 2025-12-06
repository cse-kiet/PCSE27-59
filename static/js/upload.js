/**
 * Upload functionality for fundus images
 */

document.addEventListener('DOMContentLoaded', function() {
    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const uploadForm = document.getElementById('uploadForm');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const progressContainer = document.getElementById('progressContainer');
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    const submitBtn = document.getElementById('submitBtn');
    
    // Drag and drop handlers
    if (uploadZone) {
        uploadZone.addEventListener('dragover', handleDragOver);
        uploadZone.addEventListener('dragleave', handleDragLeave);
        uploadZone.addEventListener('drop', handleDrop);
        uploadZone.addEventListener('click', () => fileInput.click());
    }
    
    // File input change handler
    if (fileInput) {
        fileInput.addEventListener('change', handleFileSelect);
    }
    
    // Form submit handler
    if (uploadForm) {
        uploadForm.addEventListener('submit', handleFormSubmit);
    }
});

/**
 * Handle drag over event
 */
function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.add('dragover');
}

/**
 * Handle drag leave event
 */
function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.remove('dragover');
}

/**
 * Handle drop event
 */
function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    e.currentTarget.classList.remove('dragover');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        const fileInput = document.getElementById('fileInput');
        fileInput.files = files;
        handleFileSelect({ target: fileInput });
    }
}

/**
 * Handle file selection
 */
function handleFileSelect(e) {
    const file = e.target.files[0];
    
    if (!file) return;
    
    // Validate file type
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
    if (!validTypes.includes(file.type)) {
        showNotification('Please select a valid image file (JPG, PNG)', 'danger');
        clearImage();
        return;
    }
    
    // Validate file size (10MB)
    const maxSize = 10 * 1024 * 1024;
    if (file.size > maxSize) {
        showNotification('File size must be less than 10MB', 'danger');
        clearImage();
        return;
    }
    
    // Show preview
    const reader = new FileReader();
    reader.onload = function(e) {
        const previewImg = document.getElementById('previewImg');
        const imagePreview = document.getElementById('imagePreview');
        
        previewImg.src = e.target.result;
        imagePreview.style.display = 'block';
        
        // Hide upload zone
        document.querySelector('.upload-content').style.display = 'none';
    };
    reader.readAsDataURL(file);
    
    showNotification(`File selected: ${file.name} (${formatFileSize(file.size)})`, 'success');
}

/**
 * Clear selected image
 */
function clearImage() {
    const fileInput = document.getElementById('fileInput');
    const imagePreview = document.getElementById('imagePreview');
    
    fileInput.value = '';
    imagePreview.style.display = 'none';
    document.querySelector('.upload-content').style.display = 'block';
}

/**
 * Handle form submission
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('fileInput');
    const patientSelect = document.getElementById('patientSelect');
    const progressContainer = document.getElementById('progressContainer');
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    const submitBtn = document.getElementById('submitBtn');
    
    // Validation
    if (!fileInput.files[0]) {
        showNotification('Please select an image file', 'warning');
        return;
    }
    
    if (!patientSelect.value) {
        showNotification('Please select a patient', 'warning');
        return;
    }
    
    // Prepare form data
    const formData = new FormData();
    formData.append('fundus_image', fileInput.files[0]);
    formData.append('patient_id', patientSelect.value);
    
    // Show progress
    progressContainer.style.display = 'block';
    submitBtn.disabled = true;
    
    // Simulate progress
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += 5;
        if (progress <= 90) {
            updateProgress(progress);
        }
    }, 100);
    
    try {
        // Upload and analyze
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        
        clearInterval(progressInterval);
        
        if (!response.ok) {
            throw new Error('Upload failed');
        }
        
        const result = await response.json();
        
        // Complete progress
        updateProgress(100);
        
        // Redirect to results
        setTimeout(() => {
            if (result.success && result.redirect) {
                window.location.href = result.redirect;
            }
        }, 500);
        
    } catch (error) {
        clearInterval(progressInterval);
        console.error('Upload error:', error);
        showNotification('Upload failed. Please try again.', 'danger');
        progressContainer.style.display = 'none';
        submitBtn.disabled = false;
    }
}

/**
 * Update progress bar
 */
function updateProgress(percent) {
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    
    progressBar.style.width = percent + '%';
    progressBar.setAttribute('aria-valuenow', percent);
    progressText.textContent = percent + '%';
}

/**
 * Format file size
 */
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

/**
 * Show notification
 */
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Prevent default drag and drop on document
document.addEventListener('dragover', function(e) {
    e.preventDefault();
});

document.addEventListener('drop', function(e) {
    e.preventDefault();
});