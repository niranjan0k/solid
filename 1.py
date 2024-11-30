# SOLID Principle with example
# 1. S => Single Repository Principle (SRP)
        # A class should have one, and only one, reason to change
    # Example
class UserManger:
    def authenticate_user(self, username, password):
        print('Authenticate user logic')

    def update_user_profile(self, user_id, new_profile_data):
        print('Profile update logic')

    def send_email_notification(self, user_email, message):
        print('User notification logic here')

# Above class violates the SRP because it has multiple responsibilities:
# Authentication, Profile Management, and Email Notifications

class UserAuthenticator:
    def authenticate_user(self, username, password):
        print('Authentication logic')
    
class UserProfileManager:
    def update_user_profile(self, user_id, new_profile_data):
        print('Profile update logic')

class EmailNotifier:
    def send_email_notification(self, user_email, message):
        print('email sending logic')

