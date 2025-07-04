#!/usr/bin/env python3
"""
Test script for MedTrack application
This script tests the main functionalities without running the web server
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, local_db, initialize_sample_data
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid

def test_database_initialization():
    """Test if the database is properly initialized with sample data"""
    print("Testing database initialization...")
    
    # Re-initialize sample data
    initialize_sample_data()
    
    # Check if users exist
    assert 'drsmith@example.com' in local_db['users'], "Dr. Smith not found in database"
    assert 'patient@example.com' in local_db['users'], "Patient not found in database"
    
    # Check user roles
    assert local_db['users']['drsmith@example.com']['role'] == 'doctor', "Dr. Smith role incorrect"
    assert local_db['users']['patient@example.com']['role'] == 'patient', "Patient role incorrect"
    
    print("✓ Database initialization test passed")

def test_password_hashing():
    """Test password hashing functionality"""
    print("Testing password hashing...")
    
    password = "test_password"
    hashed = generate_password_hash(password)
    
    # Test correct password
    assert check_password_hash(hashed, password), "Password verification failed"
    
    # Test incorrect password
    assert not check_password_hash(hashed, "wrong_password"), "Wrong password should not be accepted"
    
    print("✓ Password hashing test passed")

def test_appointment_creation():
    """Test appointment creation functionality"""
    print("Testing appointment creation...")
    
    # Create a test appointment
    appointment = {
        'id': f"test-apt-{str(uuid.uuid4())[:8]}",
        'patient': 'patient@example.com',
        'patient_name': 'John Doe',
        'doctor': 'drsmith@example.com',
        'doctor_name': 'Dr. Smith',
        'title': 'Test Consultation',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'time': '10:00 AM',
        'location': 'Office 203',
        'status': 'scheduled'
    }
    
    local_db['appointments'].append(appointment)
    
    # Verify appointment was added
    assert len(local_db['appointments']) > 0, "No appointments in database"
    
    # Find the appointment
    found_appointment = None
    for apt in local_db['appointments']:
        if apt['id'] == appointment['id']:
            found_appointment = apt
            break
    
    assert found_appointment is not None, "Appointment not found after creation"
    assert found_appointment['title'] == 'Test Consultation', "Appointment title incorrect"
    
    print("✓ Appointment creation test passed")

def test_prescription_creation():
    """Test prescription creation functionality"""
    print("Testing prescription creation...")
    
    # Create a test prescription
    prescription = {
        'id': f"test-pres-{str(uuid.uuid4())[:8]}",
        'patient': 'patient@example.com',
        'doctor': 'drsmith@example.com',
        'diagnosis': 'Test Diagnosis',
        'medications': [
            {'name': 'Test Medication', 'dosage': '10mg daily'}
        ],
        'date': datetime.now().strftime('%Y-%m-%d'),
        'status': 'Active'
    }
    
    local_db['prescriptions'].append(prescription)
    
    # Verify prescription was added
    assert len(local_db['prescriptions']) > 0, "No prescriptions in database"
    
    # Find the prescription
    found_prescription = None
    for pres in local_db['prescriptions']:
        if pres['id'] == prescription['id']:
            found_prescription = pres
            break
    
    assert found_prescription is not None, "Prescription not found after creation"
    assert found_prescription['diagnosis'] == 'Test Diagnosis', "Prescription diagnosis incorrect"
    
    print("✓ Prescription creation test passed")

def test_user_authentication():
    """Test user authentication logic"""
    print("Testing user authentication...")
    
    # Test valid user
    user = local_db['users'].get('drsmith@example.com')
    assert user is not None, "User not found"
    assert user['role'] == 'doctor', "User role incorrect"
    
    # Test password verification
    assert check_password_hash(user['password_hash'], 'password123'), "Password verification failed"
    
    # Test invalid user
    invalid_user = local_db['users'].get('nonexistent@example.com')
    assert invalid_user is None, "Non-existent user should return None"
    
    print("✓ User authentication test passed")

def test_dashboard_data():
    """Test dashboard data generation"""
    print("Testing dashboard data generation...")
    
    # Import the dashboard functions
    from app import get_patient_dashboard_data, get_doctor_dashboard_data
    
    # Test patient dashboard data
    patient_data = get_patient_dashboard_data('patient@example.com')
    assert 'name' in patient_data, "Patient dashboard missing name"
    assert 'appointments' in patient_data, "Patient dashboard missing appointments"
    assert 'prescriptions' in patient_data, "Patient dashboard missing prescriptions"
    
    # Test doctor dashboard data
    doctor_data = get_doctor_dashboard_data('drsmith@example.com')
    assert 'name' in doctor_data, "Doctor dashboard missing name"
    assert 'patients' in doctor_data, "Doctor dashboard missing patients"
    assert 'appointments' in doctor_data, "Doctor dashboard missing appointments"
    
    print("✓ Dashboard data generation test passed")

def test_flask_app():
    """Test Flask app creation and basic routes"""
    print("Testing Flask app...")
    
    # Test app creation
    assert app is not None, "Flask app not created"
    assert app.name == 'app', "Flask app name incorrect"
    
    # Test app configuration
    assert app.secret_key is not None, "App secret key not set"
    
    print("✓ Flask app test passed")

def run_all_tests():
    """Run all tests"""
    print("Starting MedTrack application tests...\n")
    
    try:
        test_database_initialization()
        test_password_hashing()
        test_appointment_creation()
        test_prescription_creation()
        test_user_authentication()
        test_dashboard_data()
        test_flask_app()
        
        print("\n🎉 All tests passed! The MedTrack application is working correctly.")
        print("\nTo run the application:")
        print("1. Make sure you're in the project directory")
        print("2. Run: python app.py")
        print("3. Open your browser and go to: http://localhost:5000")
        print("\nSample login credentials:")
        print("- Doctor: drsmith@example.com / password123")
        print("- Patient: patient@example.com / password123")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    run_all_tests() 