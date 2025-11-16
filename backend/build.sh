#!/bin/bash
# Render build script for backend

echo "Installing dependencies..."
pip install -r requirements.txt

# NOTE: Model training is SKIPPED during deployment
# Reason: Render free tier has only 512MB RAM - insufficient for training large ML models
# Solution: Train models locally and commit the .pkl files to backend/models/ directory
# 
# To train models locally:
#   cd backend
#   python train_models.py
#   git add models/*.pkl
#   git commit -m "Add trained models"
#   git push
#
# The API will load pre-trained models from backend/models/ at startup

echo "Build completed successfully!"
echo "Note: Using pre-trained models from backend/models/"
