# Quick Start Guide

## 🚀 Running the Application

### Option 1: Using the Start Script (Recommended)

Simply run the PowerShell script:

```powershell
.\start.ps1
```

This will automatically start both backend and frontend servers in separate terminal windows.

### Option 2: Manual Start

**Terminal 1 - Backend:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```

## 🌐 Access the Application

- **Frontend UI**: http://localhost:5173 or http://localhost:5174
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🎯 Using the Application

### Crop Yield Prediction
1. Navigate to the "📊 Yield Prediction" tab
2. Fill in the form with:
   - State Name (e.g., "Punjab")
   - District Name (e.g., "Amritsar")
   - Season (select from dropdown)
   - Crop Name (e.g., "Rice")
   - Area in hectares
3. Click "📊 Predict Yield"

### Crop Recommendation
1. Navigate to the "🌱 Crop Recommendation" tab
2. Enter soil and climate parameters:
   - Nitrogen (N): 0-140 kg/ha
   - Phosphorus (P): 0-145 kg/ha
   - Potassium (K): 0-205 kg/ha
   - pH: 3.5-9.9
   - Temperature: °C
   - Humidity: 0-100%
   - Rainfall: mm
3. Click "🌾 Get Recommendation"

## 🛑 Stopping the Servers

Press `Ctrl+C` in each terminal window to stop the respective server.

## 📝 Notes

- Make sure Python virtual environment is activated before running backend
- Ensure Node.js dependencies are installed (`npm install`) before running frontend
- The ML models are pre-trained and located in `backend/models/`
- Both servers support hot-reload for development

## 🔧 Troubleshooting

**Port already in use:**
- Backend: Change port in command: `uvicorn main:app --reload --port 8001`
- Frontend: Vite will automatically use the next available port (5174, 5175, etc.)

**CORS errors:**
- Check that both servers are running
- Verify CORS settings in `backend/main.py` include your frontend port

**Module not found:**
- Backend: Activate virtual environment and run `pip install -r requirements.txt`
- Frontend: Run `npm install` in the frontend directory
