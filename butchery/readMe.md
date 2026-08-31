# 32slayer butchery  - Web Application

A professional web application by Siphelele Elliot Mosoeu also known as 32slayer for an alias butchery , featuring a product catalog, user authentication, secure sessions, and an admin dashboard.

## Features
- **Product Catalog:** Browse various meat categories (Beef, Pork, Chicken, Lamb, etc.).
- **User Authentication:** Secure registration and login with password complexity requirements.
- **Admin Dashboard:** Manage products, users, and site settings.
- **Security:** CSRF protection, rate limiting, session validation, and input sanitization.
- **Cookie Consent:** Compliance with privacy regulations through a consent banner.

## Usage Steps

### 1. Setup Environment
Ensure you have the following environment variables set (optional for local testing as defaults are provided):
- `SECRET_KEY`: A long, random string for session security.
- `STRIPE_SECRET_KEY`: Your Stripe secret API key.
- `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable API key.

### 2. Install Dependencies
Run the following command to install all required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Flask development server:
```bash
python main.py
```
The application will be available at `http://127.0.0.1:5000`.

### 4. Admin Access
To access the admin dashboard:
1. Register a new account.
2. Manually set the `is_admin` flag to `True` in the `User` table of the `instance/32slayer_butchery.db` database.
3. Log in and navigate to the "Admin" link in the navigation bar.

### 5. Managing Products
- **Add Product:** Use the Admin -> Products -> Add Product form.
- **Edit/Delete:** Use the actions available in the product list view.
- **Bulk Actions:** Select multiple products to deactivate them simultaneously.

## Web Application Tutorial

Follow these steps to explore and use the 32slayer butchery web application:

### 1. Account Creation & Security
- **Registration:** Click on "Register" and create an account. Passwords must be at least 8 characters and include uppercase, lowercase, and numeric characters.
- **Cookie Consent:** Upon your first visit, you'll see a cookie banner at the bottom. Click "Accept All" to enable full session and security features.
- **Rate Limiting:** Note that registration is limited to 3 attempts per hour, and login is limited to 5 attempts per minute per IP address for your protection.

### 2. Shopping Experience
- **Browse Products:** Visit the "Home" page for featured items or "Catalog" to filter by categories like Beef, Pork, or Chicken.
- **Cart Management:** (In-progress) Add items to your cart to prepare for checkout. Your session will remain active for 30 minutes of inactivity.

### 3. Administrative Tasks (For Authorized Users)
- **Admin Dashboard:** Access the dashboard via the "Admin" link in the navigation bar (requires admin privileges).
- **Product Management:** Add new inventory with images, edit existing product details, or deactivate products that are out of stock.
- **Bulk Operations:** In the Admin Product list, you can select multiple items and deactivate them all at once using the bulk action feature.

### 4. Security & Compliance
- **Session Security:** The app uses secure, HttpOnly cookies. If you are idle for more than 30 minutes, you will be automatically logged out for security.
- **Input Safety:** All search and filter parameters are sanitized to prevent malicious exploits.

---

## Development Status
Current security features implemented:
- Rate limiting (Login: 5/min, Register: 3/hr)
- Session timeout (30 minutes)
- Secure cookie attributes
- Input sanitization for routes and bulk actions
