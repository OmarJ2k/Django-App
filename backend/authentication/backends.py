from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to find a user matching the username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # Try to find a user matching the email
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                # No user was found matching either username or email
                return None
        
        # Check the password
        if user.check_password(password):
            return user
        return None