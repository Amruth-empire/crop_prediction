# 🚀 Quick Deployment Checklist

## ✅ Pre-Deployment Checklist

- [ ] All code committed to GitHub
- [ ] **IMPORTANT: Models trained locally and committed to Git**
  ```bash
  cd backend
  python train_models.py
  git add models/*.pkl
  git commit -m "Add trained ML models"
  git push
  ```
- [ ] Verify backend/models/ directory contains:
  - `crop_yield_model.pkl`
  - `crop_recommendation_model.pkl`
  - `label_encoders.pkl`
- [ ] Backend build.sh is executable
- [ ] Environment variables configured

⚠️ **CRITICAL**: Models MUST be pre-trained and committed because:
- Render free tier has only 512MB RAM (insufficient for training)
- Training is skipped during deployment (see build.sh)
- API loads .pkl files from backend/models/ at startup

## 📝 Deployment Steps

### 1️⃣ Deploy Backend to Render (Do This First!)

1. Go to https://render.com/dashboard
2. New Web Service → Connect GitHub
3. Select repository
4. Configure:
   - Root Directory: `backend`
   - Build Command: `bash build.sh`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Wait for deployment
6. **Copy your backend URL**: `https://XXXXX.onrender.com`

### 2️⃣ Update Frontend Config

1. Edit `frontend/.env.production`:
   ```
   VITE_API_URL=https://YOUR-BACKEND-URL.onrender.com
   ```
2. Commit and push:
   ```bash
   git add .
   git commit -m "Configure production API URL"
   git push
   ```

### 3️⃣ Deploy Frontend to Vercel

1. Go to https://vercel.com/new
2. Import GitHub repository
3. Configure:
   - Root Directory: `frontend`
   - Framework: Vite
4. Add Environment Variable:
   - `VITE_API_URL` = Your Render backend URL
5. Deploy!

### 4️⃣ Test Your Deployment

- [ ] Frontend loads at Vercel URL
- [ ] Backend API docs accessible at Render URL/docs
- [ ] Crop Yield Prediction works
- [ ] Crop Recommendation works

## 🔗 Your URLs

- **Frontend**: `https://________.vercel.app`
- **Backend**: `https://________.onrender.com`
- **API Docs**: `https://________.onrender.com/docs`

## 🆘 Common Issues

**Backend 502 Error**: Wait 1 minute (cold start on free tier)
**CORS Error**: Check backend CORS includes your Vercel URL
**Build Failed**: Check Render build logs

## 📖 Full Guide

See `DEPLOYMENT.md` for detailed instructions.
