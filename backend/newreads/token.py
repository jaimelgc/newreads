from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Get the user
user = get_user_model().objects.get(username='your_username')

# Generate tokens
refresh = RefreshToken.for_user(user)
access_token = str(refresh.access_token)
refresh_token = str(refresh)

# Output the tokens
print("Access Token:", access_token)
print("Refresh Token:", refresh_token)
