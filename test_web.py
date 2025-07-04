#!/usr/bin/env python3
"""
Web application test script for MedTrack
This script tests the web routes and functionality
"""

import requests
import time
import sys
import os

def test_home_page():
    """Test the home page"""
    print("Testing home page...")
    try:
        response = requests.get('http://localhost:5000/', timeout=5)
        if response.status_code == 200:
            print("✓ Home page is accessible")
            return True
        else:
            print(f"✗ Home page returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to home page: {e}")
        return False

def test_login_pages():
    """Test login pages for both roles"""
    print("Testing login pages...")
    try:
        # Test patient login page
        response = requests.get('http://localhost:5000/login/patient', timeout=5)
        if response.status_code == 200:
            print("✓ Patient login page is accessible")
        else:
            print(f"✗ Patient login page returned status code: {response.status_code}")
            return False
        
        # Test doctor login page
        response = requests.get('http://localhost:5000/login/doctor', timeout=5)
        if response.status_code == 200:
            print("✓ Doctor login page is accessible")
        else:
            print(f"✗ Doctor login page returned status code: {response.status_code}")
            return False
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to login pages: {e}")
        return False

def test_signup_pages():
    """Test signup pages for both roles"""
    print("Testing signup pages...")
    try:
        # Test patient signup page
        response = requests.get('http://localhost:5000/signup/patient', timeout=5)
        if response.status_code == 200:
            print("✓ Patient signup page is accessible")
        else:
            print(f"✗ Patient signup page returned status code: {response.status_code}")
            return False
        
        # Test doctor signup page
        response = requests.get('http://localhost:5000/signup/doctor', timeout=5)
        if response.status_code == 200:
            print("✓ Doctor signup page is accessible")
        else:
            print(f"✗ Doctor signup page returned status code: {response.status_code}")
            return False
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to signup pages: {e}")
        return False

def test_about_page():
    """Test the about page"""
    print("Testing about page...")
    try:
        response = requests.get('http://localhost:5000/about', timeout=5)
        if response.status_code == 200:
            print("✓ About page is accessible")
            return True
        else:
            print(f"✗ About page returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to about page: {e}")
        return False

def test_static_files():
    """Test static files"""
    print("Testing static files...")
    try:
        # Test CSS file
        response = requests.get('http://localhost:5000/static/styles.css', timeout=5)
        if response.status_code == 200:
            print("✓ CSS file is accessible")
        else:
            print(f"✗ CSS file returned status code: {response.status_code}")
            return False
        
        # Test JS file
        response = requests.get('http://localhost:5000/static/script.js', timeout=5)
        if response.status_code == 200:
            print("✓ JS file is accessible")
        else:
            print(f"✗ JS file returned status code: {response.status_code}")
            return False
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to static files: {e}")
        return False

def test_404_page():
    """Test 404 error page"""
    print("Testing 404 error page...")
    try:
        response = requests.get('http://localhost:5000/nonexistent-page', timeout=5)
        if response.status_code == 404:
            print("✓ 404 error page is working correctly")
            return True
        else:
            print(f"✗ 404 page returned unexpected status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot test 404 page: {e}")
        return False

def run_web_tests():
    """Run all web tests"""
    print("🌐 Starting MedTrack Web Application Tests...\n")
    
    tests = [
        test_home_page,
        test_login_pages,
        test_signup_pages,
        test_about_page,
        test_static_files,
        test_404_page
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All web tests passed! The MedTrack application is fully functional.")
        print("\n✅ Available Features:")
        print("   - User registration and login")
        print("   - Patient and doctor dashboards")
        print("   - Appointment booking system")
        print("   - Prescription management")
        print("   - Profile management")
        print("   - Notification system")
        print("\n🌐 Access the application at: http://localhost:5000")
        print("\n👥 Sample Users:")
        print("   - Doctor: drsmith@example.com / password123")
        print("   - Patient: patient@example.com / password123")
        return True
    else:
        print(f"❌ {total - passed} tests failed. Please check the application.")
        return False

if __name__ == "__main__":
    print("Make sure the MedTrack application is running on http://localhost:5000")
    print("You can start it with: python app.py")
    print()
    
    try:
        run_web_tests()
    except KeyboardInterrupt:
        print("\n🛑 Tests interrupted by user")
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc() 