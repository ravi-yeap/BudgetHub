# 🚀 START HERE - Student Budget Manager

Welcome to the Student Budget Manager! This guide will help you get started in 5 minutes.

## ⚡ 5-Minute Quick Start (Windows)

### Step 1: Run Setup (2 minutes)
```batch
setup.bat
```
This will automatically:
- Create virtual environment
- Install dependencies
- Initialize database
- You're ready to go!

### Step 2: Start Server (1 minute)
```batch
python manage.py runserver
```

### Step 3: Open Application (1 minute)
- Open browser: **http://127.0.0.1:8000**
- Register a new account or login

### Step 4: Start Using (1 minute)
- Set your monthly budget
- Add your first expense
- View dashboard

---

## 🍎 For macOS/Linux Users

```bash
bash setup.sh
python manage.py runserver
```

Then visit: **http://127.0.0.1:8000**

---

## 📖 Documentation Structure

Read these in order:

1. **This file** (START HERE!) - You are reading it
2. **QUICKSTART.md** - Detailed setup instructions
3. **README.md** - Complete reference documentation (50+ sections)
4. **FILE_INDEX.md** - Navigate project files
5. **PROJECT_SUMMARY.md** - Project overview

---

## ✨ Key Features to Try

After you login:

### 1. Dashboard (First page)
- See financial summary
- View spending charts
- Check budget status

### 2. Add Expense
- Click "➕ Add Expense" button
- Fill in details (amount, category, date)
- Submit

### 3. Set Budget
- Go to "Budget" section
- Enter monthly limit
- See warning alerts

### 4. View Analytics
- Click "Analytics"
- See 6-month trends
- Analyze spending by category

### 5. Manage Profile
- Click your avatar (top right)
- Update profile
- Change password

---

## 🎯 First Steps Checklist

- [ ] Run setup script
- [ ] Start server
- [ ] Open http://127.0.0.1:8000
- [ ] Register account
- [ ] Set monthly budget
- [ ] Add first expense
- [ ] View dashboard
- [ ] Check analytics

---

## 🆘 Troubleshooting

### Port 8000 already in use?
```bash
python manage.py runserver 8001
```

### Virtual environment not created?
```bash
python -m venv venv
```

### Migrations failed?
```bash
python manage.py migrate
```

### Still having issues?
See **README.md** "Troubleshooting" section

---

## 📊 Demo Data (Optional)

Want to see the app with sample data?

```bash
python create_demo_data.py
```

Then login with:
- **Username**: demo
- **Password**: demo123

---

## 🔐 Admin Panel (Optional)

Manage data directly as administrator:

1. Create admin account:
   ```bash
   python manage.py createsuperuser
   ```

2. Login at: **http://127.0.0.1:8000/admin**

---

## 📝 Important URLs

- **Dashboard**: http://127.0.0.1:8000/analytics/dashboard/
- **Expenses**: http://127.0.0.1:8000/expenses/
- **Budget**: http://127.0.0.1:8000/budget/
- **Analytics**: http://127.0.0.1:8000/analytics/
- **Profile**: http://127.0.0.1:8000/profile/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 🎨 What You'll See

### Dashboard
- 3 info cards (Budget, Expenses, Balance)
- Budget progress bar
- Weekly spending chart
- Category breakdown pie chart
- Recent transactions list

### Expense Tracking
- Add, edit, delete expenses
- Filter by category & date
- Search functionality
- See all your expenses

### Budget Management
- Set monthly limit
- Track progress
- Get alerts when near limit

### Analytics
- 6-month spending trend
- Category breakdown
- Statistics and insights

---

## ⚙️ Technical Details

**Technology Stack:**
- Backend: Python Django
- Database: SQLite (automatic)
- Frontend: TailwindCSS + Chart.js
- Responsive: Works on mobile, tablet, desktop

---

## 💡 Tips

1. **Add expenses regularly** - Stay on top of spending
2. **Review analytics** - Understand spending patterns
3. **Adjust budget** - Change limit anytime
4. **Use categories** - Better organization and insights
5. **Check dashboard** - Quick overview of finances

---

## ❓ Next Questions?

**How do I...?**
- Change password? → Profile → Change Password
- Delete account? → Profile → Delete Account
- Download data? → See README.md for export options
- Deploy to production? → See README.md "Production" section

---

## 🆘 Need Help?

1. **Check README.md** (comprehensive guide)
2. **See TROUBLESHOOTING** in README.md
3. **Check FILE_INDEX.md** (find what you need)

---

## 📱 Mobile Experience

The app works perfectly on:
- ✅ iPhone/iPad
- ✅ Android phones
- ✅ Tablets
- ✅ Laptops/Desktop

---

## 🎉 You're All Set!

**Ready to manage your budget? Let's go! 💰**

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

Happy budgeting! 📊✨

---

**Questions?** → Check README.md
**Setup issues?** → Check QUICKSTART.md
**Navigation?** → Check FILE_INDEX.md
**Overview?** → Check PROJECT_SUMMARY.md

---

*Student Budget Manager - Track. Manage. Thrive.* 💪
