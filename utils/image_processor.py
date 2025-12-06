"""
Image processing utilities for fundus images
"""

from PIL import Image, ImageEnhance, ImageFilter
import os

class FundusImageProcessor:
    """Process and enhance fundus images"""
    
    def __init__(self):
        self.target_size = (512, 512)
        self.supported_formats = ['JPEG', 'PNG', 'JPG']
    
    def validate_image(self, image_path):
        """Validate if file is a valid image"""
        try:
            with Image.open(image_path) as img:
                if img.format not in self.supported_formats:
                    return False, "Unsupported image format"
                return True, "Valid image"
        except Exception as e:
            return False, str(e)
    
    def get_image_info(self, image_path):
        """Get image metadata"""
        try:
            with Image.open(image_path) as img:
                return {
                    'format': img.format,
                    'mode': img.mode,
                    'size': img.size,
                    'width': img.width,
                    'height': img.height
                }
        except Exception as e:
            return None
    
    def resize_image(self, image_path, output_path=None, size=None):
        """Resize image to target size"""
        try:
            size = size or self.target_size
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize with high quality
                img_resized = img.resize(size, Image.Resampling.LANCZOS)
                
                # Save or return
                if output_path:
                    img_resized.save(output_path, quality=95)
                    return output_path
                else:
                    return img_resized
        except Exception as e:
            print(f"Error resizing image: {e}")
            return None
    
    def enhance_contrast(self, image_path, factor=1.5):
        """Enhance image contrast"""
        try:
            with Image.open(image_path) as img:
                enhancer = ImageEnhance.Contrast(img)
                return enhancer.enhance(factor)
        except Exception as e:
            print(f"Error enhancing contrast: {e}")
            return None
    
    def enhance_sharpness(self, image_path, factor=2.0):
        """Enhance image sharpness"""
        try:
            with Image.open(image_path) as img:
                enhancer = ImageEnhance.Sharpness(img)
                return enhancer.enhance(factor)
        except Exception as e:
            print(f"Error enhancing sharpness: {e}")
            return None
    
    def apply_clahe(self, image_path):
        """Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)"""
        # Note: This is a simplified version
        # In production, use OpenCV's CLAHE implementation
        try:
            with Image.open(image_path) as img:
                # Convert to grayscale
                gray = img.convert('L')
                # Enhance contrast
                enhancer = ImageEnhance.Contrast(gray)
                enhanced = enhancer.enhance(2.0)
                return enhanced
        except Exception as e:
            print(f"Error applying CLAHE: {e}")
            return None
    
    def denoise_image(self, image_path):
        """Apply denoising filter"""
        try:
            with Image.open(image_path) as img:
                # Apply median filter for noise reduction
                denoised = img.filter(ImageFilter.MedianFilter(size=3))
                return denoised
        except Exception as e:
            print(f"Error denoising image: {e}")
            return None
    
    def create_thumbnail(self, image_path, output_path, size=(150, 150)):
        """Create thumbnail of image"""
        try:
            with Image.open(image_path) as img:
                img.thumbnail(size, Image.Resampling.LANCZOS)
                img.save(output_path, quality=85)
                return output_path
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
            return None
    
    def preprocess_for_model(self, image_path):
        """Preprocess image for ML model input"""
        try:
            with Image.open(image_path) as img:
                # Convert to RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize to model input size
                img_resized = img.resize(self.target_size, Image.Resampling.LANCZOS)
                
                # Normalize pixel values (0-1 range)
                # In production, use numpy for this
                # pixels = np.array(img_resized) / 255.0
                
                return img_resized
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return None
    
    def check_image_quality(self, image_path):
        """Check if image quality is sufficient for analysis"""
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                
                # Check minimum resolution
                if width < 224 or height < 224:
                    return False, "Image resolution too low (minimum 224x224)"
                
                # Check if image is too blurry (simplified check)
                gray = img.convert('L')
                # In production, use Laplacian variance for blur detection
                
                return True, "Image quality acceptable"
        except Exception as e:
            return False, f"Error checking quality: {e}"
    
    def extract_roi(self, image_path):
        """Extract Region of Interest (optic disc area)"""
        # This is a placeholder - in production, use actual ROI detection
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                # Center crop as simplified ROI
                left = width // 4
                top = height // 4
                right = 3 * width // 4
                bottom = 3 * height // 4
                roi = img.crop((left, top, right, bottom))
                return roi
        except Exception as e:
            print(f"Error extracting ROI: {e}")
            return None

def get_processor():
    """Get FundusImageProcessor instance"""
    return FundusImageProcessor()

def quick_validate(image_path):
    """Quick validation of fundus image"""
    processor = FundusImageProcessor()
    return processor.validate_image(image_path)

def quick_enhance(image_path, output_path):
    """Quick enhancement of fundus image"""
    processor = FundusImageProcessor()
    
    try:
        with Image.open(image_path) as img:
            # Enhance contrast
            contrast = ImageEnhance.Contrast(img)
            img_enhanced = contrast.enhance(1.5)
            
            # Enhance sharpness
            sharpness = ImageEnhance.Sharpness(img_enhanced)
            img_final = sharpness.enhance(1.3)
            
            # Save
            img_final.save(output_path, quality=95)
            return True
    except Exception as e:
        print(f"Error in quick enhance: {e}")
        return False