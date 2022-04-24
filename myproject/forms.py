
from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['name', 'introduction',
                   'address', 'phone',"secondary_phone","school_name",'ssc_percentage',
                   "hsc_college_name",'hsc_percentage',"college_or_university_name",
                   "ug_specialization", "ug_percentage","pg_percentage" ]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text', 'placeholder': 'Enter value'})

        # self.fields['name'].widget.attrs.update({'class':'input','placeholder':'Enter project name'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'body': 'Add the comments here',
            'value': 'Add your vote for the Comment'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text', 'placeholder': 'Enter value'})
