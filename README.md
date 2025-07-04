# MedTrack - Medical Appointment Management System

A comprehensive medical appointment management system built with Flask, featuring separate dashboards for doctors and patients.

## Features

### For Patients:
- User registration and authentication
- Book appointments with doctors
- View appointment history
- Receive notifications
- View prescriptions
- Health score tracking

### For Doctors:
- Patient management
- Appointment scheduling and management
- Prescription creation
- Patient history tracking
- Analytics dashboard
- Notification system

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the project root with the following variables:
```
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### 3. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Sample Users

### Doctors:
- **Dr. Smith** (Cardiology)
  - Email: drsmith@example.com
  - Password: password123

- **Dr. Johnson** (Endocrinology)
  - Email: drjohnson@example.com
  - Password: password123

- **Dr. Sai** (General Medicine)
  - Email: saikiran@gmail.com
  - Password: password123

### Patients:
- **John Doe**
  - Email: patient@example.com
  - Password: password123

## Database

The application uses an in-memory database for development. Sample data is automatically loaded when the application starts.

## API Endpoints

- `GET /` - Home page
- `GET /signup/<role>` - User registration
- `GET /login/<role>` - User login
- `GET /patient_dashboard` - Patient dashboard
- `GET /doctor_dashboard` - Doctor dashboard
- `GET /book_appointment` - Book appointment page
- `POST /book_appointment` - Create appointment
- `POST /create_prescription` - Create prescription
- `POST /update_appointment_status` - Update appointment status
- `GET /api/appointments` - Get appointments (JSON)
- `GET /api/notifications` - Get notifications (JSON)

## Project Structure

```
medtrack project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/               # Static files (CSS, JS)
│   ├── styles.css
│   └── script.js
└── templates/            # HTML templates
    ├── base.html
    ├── index.html
    ├── login.html
    ├── signup.html
    ├── patient_dashboard.html
    ├── doctor_dashboard.html
    ├── book_appoinment.html
    └── ...
```

## Development Notes

- The application uses Flask sessions for authentication
- All data is stored in memory (local_db) for development
- AWS DynamoDB integration is available but disabled by default
- Email and SNS notifications are optional features

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- Role-based access control
- Rate limiting for login attempts
- CSRF protection (Flask built-in)

## Future Enhancements

- Database persistence (PostgreSQL/MySQL)
- Real-time notifications (WebSocket)
- File upload for medical records
- Video consultation integration
- Mobile app development
- Advanced analytics and reporting 