# BudgetHub - Render Deployment Guide

## 🚀 Deploy to Render in 5 Minutes

### Step 1: Prepare Your Repository
Your code is already in GitHub: https://github.com/ravi-yeap/BudgetHub

### Step 2: Create a Render Account
1. Go to https://render.com
2. Sign up with GitHub (recommended)
3. Click "Authorize Render"

### Step 3: Deploy the Web Service
1. On Render dashboard, click **"New +"**
2. Select **"Web Service"**
3. Connect to your GitHub repo: **ravi-yeap/BudgetHub**
4. Configure:
   - **Name**: budgethub (or your choice)
   - **Environment**: Python
   - **Region**: Choose closest to you
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn config.wsgi:application`
   - **Plan**: Free (0.5 CPU, 512MB RAM)

### Step 4: Add Environment Variables
Click "Advanced" and add these environment variables:

```
DEBUG = false
ALLOWED_HOSTS = budgethub.onrender.com,*.onrender.com
SECRET_KEY = (generate a strong random key)
```

### Step 5: Deploy!
Click **"Create Web Service"** and wait for deployment (2-3 minutes)

---

## 🔐 Generate a Secure SECRET_KEY

Run this in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use an online generator: https://djecrety.ir/

---

## ✅ After Deployment

Your app will be live at: `https://budgethub.onrender.com`

**Test it:**
1. Go to https://budgethub.onrender.com
2. Click "Sign Up"
3. Create an account
4. Add expenses and track your budget!

---

## 🔄 Auto-Deploy & Updates

Render will automatically redeploy whenever you push to the `main` branch!

To update your app:
1. Make changes locally
2. Commit: `git commit -am "Update feature"`
3. Push: `git push origin main`
4. Render auto-deploys!

---

## 📊 Database

Your app uses SQLite in development. For production, you can:
- Keep SQLite (easy, works on free tier)
- Upgrade to PostgreSQL on Render (recommended for scaling)

---

## 🆘 Troubleshooting

**App failing to start?**
- Check logs: Render Dashboard → Web Service → Logs
- Ensure all env variables are set
- Check SECRET_KEY is valid

**Database errors?**
- Run migrations manually from dashboard terminal

**Static files not loading?**
- WhiteNoise middleware handles this automatically

---

## 📚 Render Documentation
https://render.com/docs
