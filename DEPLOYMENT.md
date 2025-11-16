# 🚀 Deployment Guide

Complete guide to deploy the Crop Prediction System to Vercel (frontend) and Render (backend).

---

## 📋 Prerequisites

1. **GitHub Account** - Code must be in a GitHub repository
2. **Vercel Account** - Sign up at https://vercel.com
3. **Render Account** - Sign up at https://render.com

---

## 🔧 Step 1: Prepare Your Repository

### Push to GitHub

```bash
cd D:\Crop_prediction
git add .
git commit -m "Prepare for deployment"
git push origin main
```

---

## 🖥️ Step 2: Deploy Backend to Render

### 2.1 Create New Web Service

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select the `crop_prediction` repository

### 2.2 Configure Web Service

**Basic Settings:**
- **Name**: `crop-prediction-backend`
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**: `bash build.sh`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Environment Variables:**
Click **"Advanced"** and add:
```
PYTHONUNBUFFERED=1
```

**Instance Type:**
- Select **Free** or **Starter** plan

### 2.3 Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for build to complete
3. Copy your backend URL (e.g., `https://crop-prediction-backend.onrender.com`)

### 2.4 Verify Backend

Visit: `https://your-backend-url.onrender.com/docs`

You should see the FastAPI documentation.

---

## 🌐 Step 3: Deploy Frontend to Vercel

### 3.1 Update API URL

1. Edit `frontend/.env.production`:
```env
VITE_API_URL=https://your-backend-url.onrender.com
```

2. Replace `your-backend-url.onrender.com` with your actual Render backend URL

3. Commit and push:
```bash
git add frontend/.env.production
git commit -m "Update production API URL"
git push origin main
```

### 3.2 Deploy to Vercel

**Option A: Via Vercel Dashboard**

1. Go to https://vercel.com/new
2. Import your GitHub repository
3. Configure project:
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

4. Add Environment Variable:
   - Key: `VITE_API_URL`
   - Value: `https://your-backend-url.onrender.com`

5. Click **"Deploy"**

**Option B: Via Vercel CLI**

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd frontend

# Deploy
vercel --prod
```

### 3.3 Verify Deployment

Visit your Vercel URL (e.g., `https://crop-prediction.vercel.app`)

---

## 🔄 Step 4: Update Backend CORS

After deploying frontend, update backend CORS to allow your Vercel domain:

1. Edit `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174", 
        "http://localhost:3000",
        "http://localhost",
        "https://your-frontend.vercel.app",  # Add your Vercel URL
        "https://*.vercel.app"  # Allow all Vercel preview deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

2. Commit and push:
```bash
git add backend/main.py
git commit -m "Update CORS for production"
git push origin main
```

Render will automatically redeploy the backend.

---

## ✅ Step 5: Verify Everything Works

1. **Visit Frontend**: `https://your-frontend.vercel.app`
2. **Test Crop Yield Prediction**:
   - Enter: Karnataka, Pune, Summer, Rice, 25
   - Click "Predict Yield"
   - Should see prediction result

3. **Test Crop Recommendation**:
   - Enter soil parameters
   - Click "Get Recommendation"
   - Should see crop recommendation

---

## 🎯 Important Notes

### Backend (Render)

⚠️ **Free Tier Limitations:**
- Spins down after 15 minutes of inactivity
- First request after inactivity takes 30-60 seconds (cold start)
- Upgrade to paid plan for always-on service

💡 **Model Files:**
- Models are trained during build process
- Stored in the container
- Persist across deployments

### Frontend (Vercel)

✅ **Automatic Features:**
- Auto-deploys on git push
- Preview deployments for pull requests
- Global CDN distribution
- HTTPS by default

---

## 🔧 Troubleshooting

### Backend Issues

**Build Fails:**
```bash
# Check build.sh has correct permissions
chmod +x backend/build.sh
```

**Models Not Found:**
- Ensure `build.sh` runs `train_models.py`
- Check Render build logs

**CORS Errors:**
- Add your Vercel domain to `allow_origins`
- Redeploy backend after changes

### Frontend Issues

**API Connection Failed:**
- Check `VITE_API_URL` environment variable
- Verify backend URL is correct
- Check backend is running on Render

**Build Fails:**
- Verify `package.json` has correct dependencies
- Check Vercel build logs
- Ensure `vercel.json` is configured correctly

---

## 📊 Monitoring

### Backend Health Check
```bash
curl https://your-backend-url.onrender.com/api/health
```

### Frontend
Check Vercel dashboard for:
- Build status
- Deployment logs
- Analytics

---

## 🔄 Continuous Deployment

Both services auto-deploy when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Your changes"
git push origin main

# Vercel: Deploys immediately
# Render: Deploys within 2-5 minutes
```

---

## 💰 Cost Estimates

### Free Tier (Perfect for Testing)
- **Render**: Free (with cold starts)
- **Vercel**: Free (Hobby plan)
- **Total**: $0/month

### Production (Recommended)
- **Render**: $7/month (Starter plan - always on)
- **Vercel**: Free or $20/month (Pro plan)
- **Total**: $7-27/month

---

## 🔐 Security Best Practices

1. **Environment Variables**: Never commit `.env` files
2. **API Keys**: Store in Vercel/Render environment variables
3. **CORS**: Only allow specific domains in production
4. **HTTPS**: Always enabled by default

---

## 📚 Additional Resources

- **Render Docs**: https://render.com/docs
- **Vercel Docs**: https://vercel.com/docs
- **FastAPI on Render**: https://render.com/docs/deploy-fastapi
- **Vite on Vercel**: https://vercel.com/docs/frameworks/vite

---

## 🎉 Success!

Your Crop Prediction System is now live and accessible worldwide!

- **Frontend**: https://your-frontend.vercel.app
- **Backend**: https://your-backend.onrender.com
- **API Docs**: https://your-backend.onrender.com/docs

Share your application and help farmers make better crop decisions! 🌾
