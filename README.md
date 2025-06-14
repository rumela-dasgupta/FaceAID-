# FACEAID: Face Recognition-Based Visitor Management System

**FACEAID** is a visitor management system built with **Flask**, **OpenCV**, and **DeepFace** that registers and recognizes visitors using face recognition. It captures visitor details, stores images, and matches faces for returning visitors.

---

## Features

-  Register a visitor with ID, contact, physical, and medical details
-  Capture visitor images via webcam
-  Face recognition using DeepFace (VGG-Face under the hood)
-  Visitor data stored using `pickle` in `visitor_data.dat`
-  Simple session-based profile rendering
-  Training and recognition logic modularized into `face_module.py`

---

## Technologies Used

- **Python 3.x**
- **Flask** – for the web framework
- **OpenCV** – to access webcam and capture images
- **DeepFace** – for face verification
- **HTML + Jinja2** – templating for rendering web pages
- **Pickle** – to store and retrieve visitor data

---

## Project Structure
faceaid/
│
├── main.py # Main Flask app
├── face_module.py # Contains training and recognition logic
├── visitor_data.dat # (created after registration, binary data file)
├── images/ # Stores visitor images
│ └── f101_0.png, f101_1.png ...
├── templates/
│ ├── faceaidhtml.html # Homepage
│ ├── register.html # Registration form
│ └── profile.html # Profile view
├── static/ # Optional CSS/images
├── README.md # This file

---

##  How It Works

### Registration (`/register`)
- User fills the form with visitor info.
- Captures 2 face images via webcam.
- Saves data in `visitor_data.dat` using Python `pickle`.

### Recognition (`/recognize`)
- Captures a new image via webcam.
- Compares it against all stored visitor images.
- If match found (`distance < 0.3`), profile is shown.
- If not found, visitor is prompted to register.

---

## ▶ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/faceaid.git
cd faceaid
```
### Install Dependencies

pip install flask opencv-python deepface

### Run the Application
python main.py

### Access in Browser
http://127.0.0.1:5000

