#!/bin/bash
# Render build script for backend

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Training ML models..."
python train_models.py

echo "Build completed successfully!"
