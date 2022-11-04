from wtforms_alchemy import ModelForm
from .models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        
