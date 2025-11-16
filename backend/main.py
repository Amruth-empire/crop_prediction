from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import os
from typing import Optional

app = FastAPI(
    title="Crop Yield Prediction API",
    description="API for predicting crop yield and recommending crops",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://localhost:5174", 
        "http://localhost:3000",
        "http://localhost",
        "http://localhost:80"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models and data
MODEL_DIR = "models"
DATA_DIR = "../ml"

# Request models
class CropYieldRequest(BaseModel):
    state: str
    district: str
    season: str
    crop: str
    area: float

class CropRecommendationRequest(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

# Response models
class PredictionResponse(BaseModel):
    prediction: float
    unit: str
    message: str

class RecommendationResponse(BaseModel):
    recommended_crop: str
    confidence: float
    message: str

class OptionsResponse(BaseModel):
    states: list
    districts: list
    seasons: list
    crops: list

# Global variables for models and data
crop_yield_model = None
crop_recommendation_model = None
label_encoders = None
crop_data = None

@app.on_event("startup")
async def load_models():
    """Load ML models and data on startup"""
    global crop_yield_model, crop_recommendation_model, label_encoders, crop_data
    
    try:
        # Load crop yield prediction model
        if os.path.exists(f"{MODEL_DIR}/crop_yield_model.pkl"):
            crop_yield_model = joblib.load(f"{MODEL_DIR}/crop_yield_model.pkl")
        
        # Load label encoders
        if os.path.exists(f"{MODEL_DIR}/label_encoders.pkl"):
            label_encoders = joblib.load(f"{MODEL_DIR}/label_encoders.pkl")
        
        # Load crop recommendation model
        if os.path.exists(f"{MODEL_DIR}/crop_recommendation_model.pkl"):
            crop_recommendation_model = joblib.load(f"{MODEL_DIR}/crop_recommendation_model.pkl")
        
        # Load crop data
        if os.path.exists(f"{DATA_DIR}/crop_production.csv"):
            crop_data = pd.read_csv(f"{DATA_DIR}/crop_production.csv")
            
    except Exception as e:
        print(f"Error loading models: {e}")

@app.get("/")
async def root():
    return {
        "message": "Crop Yield Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "predict_yield": "/api/predict-yield",
            "recommend_crop": "/api/recommend-crop",
            "get_options": "/api/options"
        }
    }

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "models_loaded": {
            "crop_yield": crop_yield_model is not None,
            "crop_recommendation": crop_recommendation_model is not None,
            "label_encoders": label_encoders is not None
        }
    }

@app.get("/api/options", response_model=OptionsResponse)
async def get_options():
    """Get available options for states, districts, seasons, and crops"""
    if crop_data is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    return {
        "states": sorted(crop_data['State_Name'].dropna().unique().tolist()),
        "districts": sorted(crop_data['District_Name'].dropna().unique().tolist()),
        "seasons": sorted(crop_data['Season'].dropna().unique().tolist()),
        "crops": sorted(crop_data['Crop'].dropna().unique().tolist())
    }

@app.post("/api/predict-yield", response_model=PredictionResponse)
async def predict_yield(request: CropYieldRequest):
    """Predict crop yield based on input parameters"""
    if crop_yield_model is None or label_encoders is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    try:
        # Create input dataframe
        input_data = pd.DataFrame({
            'State_Name': [request.state],
            'District_Name': [request.district],
            'Season': [request.season],
            'Crop': [request.crop],
            'Area': [request.area]
        })
        
        # Encode categorical variables
        for col in ['State_Name', 'District_Name', 'Season', 'Crop']:
            if col in label_encoders:
                le = label_encoders[col]
                # Handle unseen labels
                if input_data[col][0] in le.classes_:
                    input_data[col] = le.transform(input_data[col])
                else:
                    # Use the most frequent class
                    input_data[col] = 0
        
        # Make prediction
        prediction = crop_yield_model.predict(input_data)[0]
        
        return {
            "prediction": float(prediction),
            "unit": "tonnes",
            "message": f"Predicted yield for {request.crop} in {request.district}, {request.state}"
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

@app.post("/api/recommend-crop", response_model=RecommendationResponse)
async def recommend_crop(request: CropRecommendationRequest):
    """Recommend crop based on soil and environmental parameters"""
    if crop_recommendation_model is None:
        raise HTTPException(status_code=500, detail="Recommendation model not loaded")
    
    try:
        # Create input dataframe
        input_data = pd.DataFrame({
            'N': [request.nitrogen],
            'P': [request.phosphorus],
            'K': [request.potassium],
            'temperature': [request.temperature],
            'humidity': [request.humidity],
            'ph': [request.ph],
            'rainfall': [request.rainfall]
        })
        
        # Make prediction
        prediction = crop_recommendation_model.predict(input_data)[0]
        
        # Get probability if available
        confidence = 0.0
        if hasattr(crop_recommendation_model, 'predict_proba'):
            proba = crop_recommendation_model.predict_proba(input_data)
            confidence = float(proba[0].max())
        
        return {
            "recommended_crop": str(prediction),
            "confidence": confidence,
            "message": f"Recommended crop based on soil and environmental conditions"
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Recommendation error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
