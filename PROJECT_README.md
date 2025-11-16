# 🌾 Crop Yield Prediction System

A full-stack web application for predicting crop yields and recommending suitable crops using Machine Learning. Built with React, FastAPI, and scikit-learn.

## 🚀 Features

- **Crop Yield Prediction**: Predict crop yield based on state, district, season, crop type, and area
- **Crop Recommendation**: Get crop recommendations based on soil nutrients (NPK), pH, temperature, humidity, and rainfall
- **Interactive UI**: Modern, responsive React interface with real-time predictions
- **RESTful API**: FastAPI backend with automatic documentation
- **ML Models**: Trained Random Forest models for accurate predictions

## 📁 Project Structure

```
Crop-Yield-Prediction-in-India-using-ML/
├── backend/
│   ├── venv/                 # Python virtual environment
│   ├── models/               # Trained ML models
│   │   ├── crop_yield_model.pkl
│   │   ├── crop_recommendation_model.pkl
│   │   └── label_encoders.pkl
│   ├── main.py              # FastAPI application
│   ├── train_models.py      # Model training script
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   │   ├── CropYieldPredictor.tsx
│   │   │   └── CropRecommendation.tsx
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts
├── crop_production.csv      # Crop yield dataset
├── Crop_recommendation.csv  # Crop recommendation dataset
└── README.md
```

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.13**: Programming language
- **scikit-learn**: Machine learning library
- **pandas & numpy**: Data processing
- **joblib**: Model serialization
- **uvicorn**: ASGI server

### Frontend
- **React 19**: UI library
- **TypeScript**: Type-safe JavaScript
- **Vite**: Build tool and dev server
- **CSS3**: Styling

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ankitaS11/Crop-Yield-Prediction-in-India-using-ML.git
cd Crop-Yield-Prediction-in-India-using-ML
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Models are already trained and saved in the models/ directory
# If you need to retrain them, run:
# python train_models.py

# Start the FastAPI server
uvicorn main:app --reload
```

The backend will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

### 3. Frontend Setup

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at: `http://localhost:5173`

## 🎯 Usage

### Crop Yield Prediction

1. Open the web app at `http://localhost:5173`
2. Click on "📊 Yield Prediction" tab
3. Enter the following details:
   - State Name (e.g., Punjab, Maharashtra)
   - District Name (e.g., Amritsar, Pune)
   - Season (Kharif, Rabi, Zaid, etc.)
   - Crop Name (e.g., Rice, Wheat, Cotton)
   - Area in hectares
4. Click "📊 Predict Yield"
5. View the predicted yield in quintals per hectare

### Crop Recommendation

1. Click on "🌱 Crop Recommendation" tab
2. Enter soil and climate parameters:
   - Nitrogen (N) content (kg/ha)
   - Phosphorus (P) content (kg/ha)
   - Potassium (K) content (kg/ha)
   - pH level
   - Temperature (°C)
   - Humidity (%)
   - Rainfall (mm)
3. Click "🌾 Get Recommendation"
4. View the recommended crop with confidence score

## 📊 API Endpoints

### GET `/`
Health check endpoint

### POST `/predict-yield`
Predict crop yield

**Request Body:**
```json
{
  "state": "Punjab",
  "district": "Amritsar",
  "season": "Kharif",
  "crop": "Rice",
  "area": 100
}
```

**Response:**
```json
{
  "prediction": 25.5,
  "unit": "quintals/hectare",
  "message": "Predicted yield for Rice in Amritsar, Punjab during Kharif season"
}
```

### POST `/recommend-crop`
Recommend suitable crop

**Request Body:**
```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "temperature": 20.5,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 202
}
```

**Response:**
```json
{
  "recommended_crop": "Rice",
  "confidence": 95.5,
  "message": "Based on the provided conditions, Rice is recommended"
}
```

### GET `/stats`
Get dataset statistics

### GET `/available-crops`
Get list of available crops

### GET `/available-states`
Get list of available states

## 🧪 Model Information

### Crop Yield Prediction Model
- **Algorithm**: Random Forest Regressor
- **Features**: State, District, Season, Crop, Area
- **Target**: Yield (Production/Area)
- **Dataset**: 246,091 records from Indian crop production data

### Crop Recommendation Model
- **Algorithm**: Random Forest Classifier
- **Features**: N, P, K, Temperature, Humidity, pH, Rainfall
- **Target**: Crop type
- **Dataset**: Agricultural soil and climate data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👥 Authors

- **Ankita Singh** - [@ankitaS11](https://github.com/ankitaS11)

## 🙏 Acknowledgments

- Dataset source: Indian Agriculture Data
- Machine Learning: scikit-learn
- Web Framework: FastAPI & React

## 📧 Contact

For any queries or suggestions, please open an issue on GitHub.

---

Made with ❤️ for Indian Agriculture
