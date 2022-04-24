from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Skill,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels ={
            'first_name': 'Name',
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','username','location','location',
        'email','short_intro','bio','profile_image','social_github',
        'social_twitter','social_youtube']
    
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            for label,field in self.fields.items():
                field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})




class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude =['owner']
        

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            for label,field in self.fields.items():
                field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})



class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
        
        

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            for label,field in self.fields.items():
                field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})
