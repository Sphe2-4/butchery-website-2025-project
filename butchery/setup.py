
#!/usr/bin/env python3
"""
Setup script for 32slayer butchery Web Application
Run this script to configure your Stripe and Twilio credentials
"""

import os
import sys

def main():
    print("=" * 60)
    print("32slayer butchery Web Application Setup")
    print("=" * 60)
    print()
    
    print("To complete the setup, you'll need:")
    print("1. Stripe Test API Keys (from https://dashboard.stripe.com/test/apikeys)")
    print("2. Twilio Account Credentials (from https://console.twilio.com/)")
    print()
    
    # Get Stripe credentials
    print("STRIPE CONFIGURATION:")
    print("Get your test keys from: https://dashboard.stripe.com/test/apikeys")
    stripe_secret = input("Enter Stripe Secret Key (sk_test_...): ").strip()
    stripe_public = input("Enter Stripe Publishable Key (pk_test_...): ").strip()
    print()
    
    # Get Twilio credentials
    print("TWILIO CONFIGURATION:")
    print("Get your credentials from: https://console.twilio.com/")
    twilio_sid = input("Enter Twilio Account SID: ").strip()
    twilio_token = input("Enter Twilio Auth Token: ").strip()
    twilio_phone = input("Enter Twilio Phone Number (+1234567890): ").strip()
    print()
    
    # Update main.py with the credentials
    try:
        with open('main.py', 'r') as f:
            content = f.read()
        
        # Replace placeholder values
        content = content.replace('stripe.api_key = "sk_test_51..."', f'stripe.api_key = "{stripe_secret}"')
        content = content.replace('STRIPE_PUBLISHABLE_KEY = "pk_test_51..."', f'STRIPE_PUBLISHABLE_KEY = "{stripe_public}"')
        content = content.replace('TWILIO_ACCOUNT_SID = "your_twilio_account_sid"', f'TWILIO_ACCOUNT_SID = "{twilio_sid}"')
        content = content.replace('TWILIO_AUTH_TOKEN = "your_twilio_auth_token"', f'TWILIO_AUTH_TOKEN = "{twilio_token}"')
        content = content.replace('TWILIO_PHONE_NUMBER = "your_twilio_phone_number"', f'TWILIO_PHONE_NUMBER = "{twilio_phone}"')
        
        with open('main.py', 'w') as f:
            f.write(content)
        
        print(" Configuration updated successfully!")
        print()
        print("NEXT STEPS:")
        print("1. Run the application: python main.py")
        print("2. Open your browser to: http://localhost:5000")
        print("3. Login as admin with username: Siphelele23, password: Admin123!")
        print()
        print("IMPORTANT SECURITY NOTES:")
        print("- This setup uses test credentials - suitable for development only")
        print("- For production, use environment variables for sensitive data")
        print("- Replace test Stripe keys with live keys for real payments")
        print("- Enable HTTPS for production deployment")
        print()
        
    except Exception as e:
        print(f" Error updating configuration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
