"""
Train and save machine learning models for crop yield prediction and recommendation
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Create models directory
os.makedirs('models', exist_ok=True)

print("Loading crop production data...")
# Load crop production data
crop_data = pd.read_csv('../ml/crop_production.csv')

# Data preprocessing for yield prediction
print("\nPreprocessing data for yield prediction...")
# Remove rows with missing values
crop_data_clean = crop_data.dropna()

# Create label encoders for categorical variables
label_encoders = {}
categorical_cols = ['State_Name', 'District_Name', 'Season', 'Crop']

for col in categorical_cols:
    le = LabelEncoder()
    crop_data_clean[col] = le.fit_transform(crop_data_clean[col])
    label_encoders[col] = le

# Prepare features and target for yield prediction
X_yield = crop_data_clean[['State_Name', 'District_Name', 'Season', 'Crop', 'Area']]
y_yield = crop_data_clean['Production']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_yield, y_yield, test_size=0.2, random_state=42)

# Train Random Forest model for yield prediction (optimized for smaller file size)
print("\nTraining Random Forest model for yield prediction...")
# Reduced parameters to minimize model size while maintaining accuracy:
# - n_estimators: 50 instead of 100 (fewer trees = smaller model)
# - max_depth: 15 (limit tree depth to reduce complexity)
# - min_samples_split: 10 (prevents overfitting, reduces size)
# - min_samples_leaf: 4 (smoother predictions, smaller trees)
rf_model = RandomForestRegressor(
    n_estimators=50,
    max_depth=15,
    min_samples_split=10,
    min_samples_leaf=4,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

# Evaluate model
train_score = rf_model.score(X_train, y_train)
test_score = rf_model.score(X_test, y_test)
print(f"Training Score: {train_score:.4f}")
print(f"Testing Score: {test_score:.4f}")

# Save the model and encoders with compression
print("\nSaving crop yield prediction model...")
# compress=3 reduces file size significantly (level 0-9, 3 is good balance)
joblib.dump(rf_model, 'models/crop_yield_model.pkl', compress=3)
joblib.dump(label_encoders, 'models/label_encoders.pkl', compress=3)

print("\n" + "="*50)
print("Crop yield prediction model saved successfully!")
print("="*50)

# Train crop recommendation model if data exists
if os.path.exists('../ml/Crop_recommendation.csv'):
    print("\nLoading crop recommendation data...")
    crop_rec_data = pd.read_csv('../ml/Crop_recommendation.csv')
    
    print("Training crop recommendation model...")
    X_rec = crop_rec_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y_rec = crop_rec_data['label']
    
    X_train_rec, X_test_rec, y_train_rec, y_test_rec = train_test_split(
        X_rec, y_rec, test_size=0.2, random_state=42
    )
    
    # Optimized Random Forest for smaller model size
    rf_rec_model = RandomForestClassifier(
        n_estimators=50,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=4,
        random_state=42,
        n_jobs=-1
    )
    rf_rec_model.fit(X_train_rec, y_train_rec)
    
    train_score_rec = rf_rec_model.score(X_train_rec, y_train_rec)
    test_score_rec = rf_rec_model.score(X_test_rec, y_test_rec)
    print(f"Training Score: {train_score_rec:.4f}")
    print(f"Testing Score: {test_score_rec:.4f}")
    
    # Save recommendation model with compression
    print("\nSaving crop recommendation model...")
    joblib.dump(rf_rec_model, 'models/crop_recommendation_model.pkl', compress=3)
    
    print("\n" + "="*50)
    print("Crop recommendation model saved successfully!")
    print("="*50)
else:
    print("\nCrop recommendation dataset not found. Skipping recommendation model training.")

print("\n✅ Model training completed!")
print("\nSaved files:")
print("  - models/crop_yield_model.pkl")
print("  - models/label_encoders.pkl")
if os.path.exists('models/crop_recommendation_model.pkl'):
    print("  - models/crop_recommendation_model.pkl")
