# 🌾 Crop Yield Prediction & Recommendation System

A comprehensive machine learning application for predicting crop yields and recommending optimal crops based on soil and environmental conditions. This full-stack solution combines data science, backend API, and a modern web interface to help farmers make informed agricultural decisions.

## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Information](#model-information)
- [Contributing](#contributing)

## ✨ Features

### 🌱 Crop Yield Prediction
- Predict crop yield based on:
  - State and District location
  - Season (Kharif, Rabi, Zaid, etc.)
  - Crop type
  - Cultivation area (hectares)
- Achieved **88.83%** test accuracy using Random Forest Regression

### 🎯 Crop Recommendation
- Get crop recommendations based on:
  - Soil nutrients (N, P, K levels)
  - Environmental factors (Temperature, Humidity, Rainfall)
  - Soil pH level
- Achieved **99.32%** test accuracy using Random Forest Classification

### 🎨 Modern Web Interface
- Responsive React-based frontend
- Real-time predictions
- User-friendly forms with validation
- Clean and intuitive UI design

### 🚀 RESTful API
- FastAPI backend with automatic documentation
- CORS-enabled for easy integration
- Health check endpoints
- Comprehensive error handling

## 📁 Project Structure

```
crop_prediction/
├── backend/                    # FastAPI Backend
│   ├── models/                # Trained ML models
│   │   ├── crop_yield_model.pkl
│   │   ├── crop_recommendation_model.pkl
│   │   └── label_encoders.pkl
│   ├── main.py               # API endpoints
│   ├── train_models.py       # Model training script
│   ├── requirements.txt      # Python dependencies
│   └── venv/                 # Virtual environment
│
├── frontend/                  # React + Vite Frontend
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── CropYieldPredictor.tsx
│   │   │   ├── CropRecommendation.tsx
│   │   │   └── *.css
│   │   ├── App.tsx          # Main app component
│   │   └── main.tsx         # Entry point
│   ├── public/              # Static assets
│   ├── package.json         # Node dependencies
│   └── vite.config.ts       # Vite configuration
│
├── ml/                       # Machine Learning Research
│   ├── Crop prediction model .ipynb
│   ├── Crop recommendation .ipynb
│   ├── Crop_Recommendation_Testing_Final.ipynb
│   ├── Data Analysis & Visualization - crop yield dataset.ipynb
│   ├── crop_production.csv  # Training dataset
│   └── Crop_recommendation.csv
│
├── start.ps1                # Quick start script
├── QUICKSTART.md            # Quick start guide
└── README.md                # This file
```

## 🛠️ Technologies Used

### Backend
- **Python 3.13**
- **FastAPI** - Modern web framework for building APIs
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation and analysis
- **joblib** - Model serialization
- **uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool and dev server
- **CSS3** - Styling

### Machine Learning
- **Random Forest Regressor** - Crop yield prediction
- **Random Forest Classifier** - Crop recommendation
- **Label Encoding** - Categorical variable handling

## 📦 Installation

### Prerequisites
- **Python 3.10+** installed
- **Node.js 16+** and npm installed
- Git (optional)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Amruth-empire/crop_prediction.git
cd crop_prediction
```

### Step 2: Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows Command Prompt:
.\venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the models (required for first run)
python train_models.py
```

### Step 3: Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install
```

## 🚀 Usage

### Quick Start (Recommended)
Run the PowerShell script to start both servers automatically:
```powershell
.\start.ps1
```

### Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\Activate.ps1  # Windows
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Access the Application
- **Frontend UI**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/api/health

## 📚 API Documentation

### Endpoints

#### `GET /api/health`
Check API health and model loading status.

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": {
    "crop_yield": true,
    "crop_recommendation": true,
    "label_encoders": true
  }
}
```

#### `POST /api/predict-yield`
Predict crop yield based on input parameters.

**Request Body:**
```json
{
  "state": "Punjab",
  "district": "Amritsar",
  "season": "Kharif",
  "crop": "Rice",
  "area": 100.5
}
```

**Response:**
```json
{
  "prediction": 245.8,
  "unit": "tonnes",
  "message": "Predicted yield for Rice in Amritsar, Punjab"
}
```

#### `POST /api/recommend-crop`
Recommend crop based on soil and environmental conditions.

**Request Body:**
```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "temperature": 20.5,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 200
}
```

**Response:**
```json
{
  "recommended_crop": "rice",
  "confidence": 0.95,
  "message": "Recommended crop based on soil and environmental conditions"
}
```

#### `GET /api/options`
Get available options for states, districts, seasons, and crops.

**Response:**
```json
{
  "states": ["Andhra Pradesh", "Karnataka", "Punjab", ...],
  "districts": ["Amritsar", "Bangalore", "Pune", ...],
  "seasons": ["Kharif", "Rabi", "Zaid", "Summer", ...],
  "crops": ["Rice", "Wheat", "Cotton", "Sugarcane", ...]
}
```

## 🤖 Model Information

### Crop Yield Prediction Model
- **Algorithm**: Random Forest Regressor
- **Features**: State, District, Season, Crop, Area
- **Training Score**: 97.97%
- **Testing Score**: 88.83%
- **Dataset**: Historical crop production data from India

### Crop Recommendation Model
- **Algorithm**: Random Forest Classifier
- **Features**: N, P, K, Temperature, Humidity, pH, Rainfall
- **Training Score**: 100%
- **Testing Score**: 99.32%
- **Dataset**: Soil and crop characteristics dataset

### Model Training
To retrain the models with updated data:
```bash
cd backend
python train_models.py
```

This will:
1. Load data from `ml/` directory
2. Preprocess and encode features
3. Train both models
4. Save models to `backend/models/` directory
5. Display training and testing scores

## 🔧 Configuration

### Backend Configuration
Edit `backend/main.py` to modify:
- CORS origins
- Model directory paths
- API endpoints

### Frontend Configuration
Edit `frontend/vite.config.ts` to modify:
- Development server port
- Build output directory
- Proxy settings

## 🐛 Troubleshooting

### Port Already in Use
- **Backend**: Change port with `uvicorn main:app --reload --port 8001`
- **Frontend**: Vite automatically tries the next available port

### Module Not Found Errors
- **Backend**: Activate venv and run `pip install -r requirements.txt`
- **Frontend**: Run `npm install` in frontend directory

### CORS Errors
- Ensure both servers are running
- Check CORS origins in `backend/main.py`

### Model Not Found
- Run `python train_models.py` in backend directory
- Ensure CSV files exist in `ml/` directory

## 📊 Dataset Information

### Crop Production Dataset
- **Source**: Indian agricultural data
- **Records**: Historical crop production data
- **Features**: State, District, Season, Crop, Area, Production

### Crop Recommendation Dataset
- **Features**: N, P, K, Temperature, Humidity, pH, Rainfall
- **Target**: Crop label (22 different crops)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👥 Authors

- **Amruth** - [Amruth-empire](https://github.com/Amruth-empire)

## 🙏 Acknowledgments

- Indian agricultural datasets
- scikit-learn community
- FastAPI and React communities

---

**Built with React, FastAPI & Machine Learning | Data-driven agriculture solutions**
