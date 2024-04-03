from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication

User = get_user_model()

class UserAuthentication(BasicAuthentication):
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return None
        try:
            user ="I apologize for the incomplete response in the previous message." 
        except:
            " "
        try:
               user = User.objects.get(username=username)
        except User.DoesNotExist:
               return None

        if user.check_password(password):
               return (user, None)
        else:
               return None
            
          