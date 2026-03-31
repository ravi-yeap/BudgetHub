# 📊 Student Budget Manager

A modern, responsive web application for student expense tracking and budget management built with Django, SQLite, and Chart.js.

## Features

✨ **Core Features:**
- 🔐 User registration, login, and authentication
- 📊 Interactive dashboard with real-time analytics
- 💸 Comprehensive expense tracking and management
- 💰 Monthly budget planning and monitoring
- 📈 Visual charts and spending analytics
- 🏪 Category-based expense organization
- 🔍 Search and filter expenses
- 👤 User profile management
- 🎨 Dark theme, responsive UI

## Technology Stack

```
Backend:      Django 4.2.11
Database:     SQLite (db.sqlite3)
Frontend:     Django Templates
Styling:      TailwindCSS
Charts:       Chart.js
Python:       3.8+
```

## Project Structure

```
student_budget_manager/
│
├── accounts/               # User authentication & profiles
│   ├── models.py          # StudentProfile model
│   ├── views.py           # Auth views (signup, login, logout)
│   ├── forms.py           # Auth forms
│   ├── urls.py
│   └── admin.py
│
├── expenses/              # Expense management
│   ├── models.py          # Expense model
│   ├── views.py           # Expense CRUD operations
│   ├── forms.py           # Expense forms
│   ├── urls.py
│   └── admin.py
│
├── budget/                # Budget management
│   ├── views.py           # Budget views
│   ├── forms.py           # Budget forms
│   ├── urls.py
│   └── models.py
│
├── analytics/             # Dashboard & analytics
│   ├── views.py           # Dashboard, analytics views
│   ├── urls.py
│   └── models.py
│
├── config/                # Django configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── __init__.py
│
├── templates/             # HTML templates
│   ├── base.html          # Base template with sidebar
│   ├── accounts/          # Auth templates
│   ├── dashboard/         # Dashboard templates
│   ├── expenses/          # Expense templates
│   └── budget/            # Budget templates
│
├── static/                # Static files
│   ├── css/
│   └── js/
│
├── manage.py              # Django management
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone or Download

```bash
# If using git
git clone <repository-url>
cd student_budget_manager

# Or extract the provided ZIP file and navigate to the directory
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) and initializes all tables.

### Step 5: Create Superuser (Admin Account) [Optional]

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. This allows you to access `/admin` for database management.

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000**

## Usage Guide

### First Time Users

1. **Register Account**
   - Navigate to `/register`
   - Fill in: First Name, Last Name, Email, Username, Password
   - Click "Create Account"

2. **Login**
   - Go to `/login`
   - Enter your username/email and password
   - Click "Sign In"

3. **Set Monthly Budget**
   - Click "Budget" in the sidebar
   - Enter your monthly budget limit
   - Click "Update Budget"

4. **Add Expenses**
   - Click "➕ Add Expense" button
   - Fill in: Title, Amount, Category, Date, Notes (optional)
   - Click "Add Expense"

5. **View Analytics**
   - Dashboard shows: total budget, expenses, remaining balance
   - Charts display: weekly spending, category breakdown
   - Recent transactions appear at the bottom

### Main Dashboard

The dashboard displays:
- **Total Monthly Budget**: Your set limit
- **Total Expenses**: Sum of all recorded expenses
- **Remaining Balance**: Budget - Total Expenses
- **Budget Progress**: Visual percentage indicator
- **Weekly Spending Chart**: Bar chart of daily spending
- **Category Breakdown**: Pie/donut chart of expenses by category
- **Recent Transactions**: Last 5 expenses with quick view

### Expense Management

**View All Expenses**: Click "Expenses" in sidebar
- Filter by category, date range
- Search by title or notes
- Edit or delete individual expense
- See total count and amount

**Add Expense**: Click "➕ Add Expense"
- Title: Description of expense
- Amount: Numerical value
- Category: Select from predefined list
- Date: When the expense occurred
- Notes: Optional additional information

**Edit Expense**: Click pencil icon next to expense
- Modify any field
- Save changes

**Delete Expense**: Click trash icon next to expense
- Confirm deletion

### Budget Management

1. Go to "Budget" section
2. View current budget setting
3. Enter new budget amount
4. Click "Update Budget"

**Budget Alerts:**
- ✅ **Green**: Using less than 80%
- ⚠️ **Yellow**: Using 80-99%
- 🔴 **Red**: Budget exceeded (100%+)

### Analytics & Reports

1. Go to "Analytics" in sidebar
2. View:
   - Total expenses this month
   - Total transactions count
   - Average expense amount
   - 6-month trend chart
   - Category distribution
   - Detailed breakdown table

### Profile Settings

1. Click user avatar in sidebar
2. Select "👤 Profile"
3. View current information
4. Options:
   - **Edit Profile**: Update name and email
   - **Change Password**: Update login password
   - **Delete Account**: Permanently delete account (⚠️ irreversible)

## API Endpoints

### Authentication
- `GET /login/` - Login page
- `POST /login/` - Submit login
- `GET /register/` - Registration page
- `POST /register/` - Submit registration
- `GET /logout/` - Logout
- `GET /profile/` - View profile

### Expenses
- `GET /expenses/` - List all expenses
- `POST /expenses/add/` - Create expense
- `POST /expenses/<id>/edit/` - Edit expense
- `POST /expenses/<id>/delete/` - Delete expense

### Budget
- `GET /budget/` - View budget
- `POST /budget/` - Update budget

### Dashboard
- `GET /analytics/dashboard/` - Main dashboard
- `GET /analytics/` - Analytics page

## Categories

Available expense categories:
- 🍔 Food
- 🚗 Transport
- 🏠 Rent
- 💡 Utilities
- 🎬 Entertainment
- 📚 Stationery
- 📦 Other

## Database Models

### StudentProfile
```python
- user (OneToOneField to User)
- monthly_budget (DecimalField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Expense
```python
- user (ForeignKey to User)
- title (CharField)
- amount (DecimalField)
- category (CharField with choices)
- date (DateField)
- notes (TextField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

## Admin Panel

Access Django admin at `/admin` after creating a superuser:

```bash
python manage.py createsuperuser
```

Manage:
- User accounts
- Student profiles
- Expense records
- System statistics

## Security Features

✅ **Implemented Security:**
- Password hashing (Django default)
- CSRF protection on all forms
- Session authentication
- Protected routes (login required)
- SQL injection prevention
- XSS protection headers
- Secure password validation

## Customization

### Change Theme Colors

Edit `templates/base.html` and modify tailwind color classes:
```html
from-blue-600 to-blue-700  → Change to your color
text-blue-500 → Change primary color
```

### Add New Categories

Edit `expenses/models.py`:
```python
CATEGORY_CHOICES = [
    ('your_category', 'Display Name'),
    # Add more...
]
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Customize Budget Settings

Edit `config/settings.py` to adjust:
- Session timeout
- Security settings
- Database configuration
- Static files location

## Troubleshooting

### Issue: "No such table: accounts_studentprofile"

**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: Port 8000 already in use

**Solution**: Use different port
```bash
python manage.py runserver 8001
```

### Issue: Static files not loading

**Solution**: Collect static files
```bash
python manage.py collectstatic --noinput
```

### Issue: Login redirects to /login repeatedly

**Solution**: Check:
1. Ensure migrations are run
2. Clear browser cache
3. Delete `db.sqlite3` and re-migrate if needed

## Production Deployment

**Before deploying to production:**

1. Change `DEBUG = False` in `config/settings.py`
2. Set `SECRET_KEY` to a secure random value
3. Update `ALLOWED_HOSTS` with your domain
4. Set `SESSION_COOKIE_SECURE = True`
5. Set `CSRF_COOKIE_SECURE = True`
6. Use environment variables for sensitive data
7. Set up proper database (PostgreSQL recommended)
8. Configure HTTPS/SSL
9. Use a production WSGI server (Gunicorn, uWSGI)

## Performance Tips

- Use `select_related()` and `prefetch_related()` for queries
- Enable database query caching
- Minify CSS/JavaScript in production
- Use CDN for static files
- Implement pagination for large expense lists

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Common Django Commands

```bash
# Create new app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
- Check existing documentation
- Review error messages carefully
- Check Django official documentation
- Feel free to reach out

## Changelog

### Version 1.0.0 (Current)
- Initial release
- User authentication
- Expense tracking
- Budget management
- Dashboard analytics
- Dark theme UI
- Responsive design

## Roadmap

Future features:
- 📱 Mobile app
- 📧 Email notifications
- 📥 CSV/PDF export
- 🔄 Recurring expenses
- 👥 Shared budgets
- 💳 Payment integration
- 📊 Advanced analytics
- 🌙 Light theme
- 🔐 Two-factor authentication

## Contact & Resources

- Django Documentation: https://docs.djangoproject.com/
- TailwindCSS: https://tailwindcss.com/
- Chart.js: https://www.chartjs.org/
- Python: https://www.python.org/

---

**Happy Budget Managing! 💰✨**

Made with ❤️ for students
