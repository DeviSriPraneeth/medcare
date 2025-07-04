#!/usr/bin/env python3
"""
Startup script for MedTrack application
This script provides a simple way to run the application with proper configuration
"""

import os
import sys
from app import app, initialize_sample_data

def main():
    """Main function to start the MedTrack application"""
    print("🚀 Starting MedTrack - Medical Appointment Management System")
    print("=" * 60)
    
    # Initialize sample data
    print("📊 Initializing database with sample data...")
    initialize_sample_data()
    print("✅ Database initialized successfully")
    
    # Set default configuration if not already set
    if not app.secret_key or app.secret_key == os.urandom(24):
        app.secret_key = 'medtrack-secret-key-change-in-production'
    
    print("\n📋 Application Information:")
    print(f"   - Flask Version: {app.config.get('ENV', 'development')}")
    print(f"   - Debug Mode: {app.debug}")
    print(f"   - Secret Key: {'Set' if app.secret_key else 'Not Set'}")
    
    print("\n👥 Sample Users Available:")
    print("   Doctors:")
    print("     - drsmith@example.com (Cardiology) - password: password123")
    print("     - drjohnson@example.com (Endocrinology) - password: password123")
    print("     - saikiran@gmail.com (General Medicine) - password: password123")
    print("   Patients:")
    print("     - patient@example.com - password: password123")
    
    print("\n🌐 Starting web server...")
    print("   - Local URL: http://localhost:5000")
    print("   - Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Run the application
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("Thank you for using MedTrack!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 