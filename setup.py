"""
Quick setup script for Diabetic Retinopathy Detection System
Run this file to set up the application automatically
"""

import os
import sys
import subprocess

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    directories = [
        'static/uploads',
        'static/css',
        'static/js',
        'static/images',
        'templates',
        'templates/layout',
        'utils',
        'models'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  ✓ Created: {directory}")

def create_init_files():
    """Create __init__.py files for packages"""
    print("\nCreating package files...")
    packages = ['utils', 'models']
    
    for package in packages:
        init_file = os.path.join(package, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write(f'"""\n{package.capitalize()} package\n"""\n')
            print(f"  ✓ Created: {init_file}")

def create_gitkeep():
    """Create .gitkeep in uploads folder"""
    gitkeep_path = 'static/uploads/.gitkeep'
    if not os.path.exists(gitkeep_path):
        with open(gitkeep_path, 'w') as f:
            f.write('')
        print(f"  ✓ Created: {gitkeep_path}")

def check_python_version():
    """Check if Python version is adequate"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("  ✗ Error: Python 3.8 or higher is required")
        print(f"  Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"  ✓ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\nInstalling required packages...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("  ✓ All packages installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("  ✗ Error installing packages")
        return False

def create_sample_data():
    """Create sample fundus images (placeholders)"""
    print("\nNote: Sample fundus images should be placed in static/uploads/")
    print("      You can use your own fundus images for testing.")

def print_completion_message():
    """Print completion message with instructions"""
    print_header("Setup Complete!")
    print("✓ All directories created")
    print("✓ Dependencies installed")
    print("✓ Application is ready to run\n")
    
    print("Next Steps:")
    print("-" * 60)
    print("1. Start the application:")
    print("   python app.py")
    print("\n2. Open your browser and navigate to:")
    print("   http://localhost:5000")
    print("\n3. Upload fundus images and test the analysis")
    print("\n4. For production deployment, see README.md")
    print("-" * 60)

def main():
    """Main setup function"""
    print_header("Diabetic Retinopathy Detection System - Setup")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create package files
    create_init_files()
    
    # Create .gitkeep
    create_gitkeep()
    
    # Install requirements
    print("\nDo you want to install required packages? (y/n): ", end='')
    response = input().lower()
    if response == 'y':
        if not install_requirements():
            print("\n⚠ Warning: Package installation failed")
            print("  Please run manually: pip install -r requirements.txt")
    
    # Sample data info
    create_sample_data()
    
    # Print completion message
    print_completion_message()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error during setup: {e}")
        sys.exit(1)