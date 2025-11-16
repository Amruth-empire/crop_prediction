# 🌐 Smart Krishi AI - Deployment URLs

## 🚀 Production Environment

### Frontend (Vercel)
- **URL**: https://smart-krishi-ai.vercel.app
- **Platform**: Vercel
- **Auto-Deploy**: Yes (on git push to main)

### Backend API (Render)
- **URL**: https://crop-prediction-pguj.onrender.com
- **API Docs**: https://crop-prediction-pguj.onrender.com/docs
- **Health Check**: https://crop-prediction-pguj.onrender.com/api/health
- **Platform**: Render
- **Auto-Deploy**: Yes (on git push to main)

---

## 💻 Local Development

### Frontend
```bash
cd frontend
npm run dev
# Runs on: http://localhost:5173
```

### Backend
```bash
cd backend
.\venv\Scripts\Activate.ps1  # Windows
uvicorn main:app --reload
# Runs on: http://localhost:8000
```

---

## 🔧 Environment Configuration

### Local Development
- Frontend connects to: `http://localhost:8000`
- Configured in: `frontend/.env.development`

### Production
- Frontend connects to: `https://crop-prediction-pguj.onrender.com`
- Configured in: `frontend/.env.production`

---

## 📊 Testing the Deployment

### Test Backend API
```bash
# Health check
curl https://crop-prediction-pguj.onrender.com/api/health

# Get available options
curl https://crop-prediction-pguj.onrender.com/api/options
```

### Test Frontend
1. Visit: https://smart-krishi-ai.vercel.app
2. Try **Crop Yield Prediction**:
   - State: Karnataka
   - District: Bangalore
   - Season: Kharif
   - Crop: Rice
   - Area: 10
3. Try **Crop Recommendation**:
   - N: 90, P: 42, K: 43
   - Temperature: 20, Humidity: 82
   - pH: 6.5, Rainfall: 200

---

## 🔄 Deployment Workflow

### Update & Deploy
```bash
# Make your changes
git add .
git commit -m "Your changes"
git push origin main

# Automatic deployments:
# ✅ Vercel: Deploys immediately (~1-2 minutes)
# ✅ Render: Deploys within 2-5 minutes
```

### Check Deployment Status
- **Vercel**: https://vercel.com/dashboard
- **Render**: https://dashboard.render.com

---

## 🆘 Troubleshooting

### Backend 502 Error
⏳ **Wait 30-60 seconds** - Render free tier spins down after 15 minutes of inactivity

### CORS Error
✅ Already configured for:
- `https://smart-krishi-ai.vercel.app`
- All `*.vercel.app` preview deployments
- Local development ports

### API Not Responding
1. Check backend health: https://crop-prediction-pguj.onrender.com/api/health
2. Check Render logs in dashboard
3. Verify models are loaded (check startup logs)

---

## 📱 Share Your App

**Production URL**: https://smart-krishi-ai.vercel.app

Perfect for:
- 👨‍🌾 Farmers seeking crop recommendations
- 🎓 Students learning ML applications
- 💼 Portfolio showcase
- 🌾 Agricultural research

---

## 🔒 Security Notes

✅ HTTPS enabled on both frontend and backend
✅ CORS properly configured
✅ Environment variables secured in Vercel/Render dashboards
✅ Pre-trained models (~10 MB) loaded at startup

---

## 💰 Current Plan

- **Vercel**: Free (Hobby tier)
- **Render**: Free (with cold starts)
- **Total Cost**: $0/month

**Upgrade Options**:
- Render Starter ($7/month) - No cold starts, always-on
- Vercel Pro ($20/month) - More builds, analytics

---

**Last Updated**: November 16, 2025
