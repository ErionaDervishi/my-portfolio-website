from django import forms
from .models import AboutMe, Contact_model, Project_model

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['content']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_model
        fields = ['email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_model
        fields = ['title', 'description', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            allowed_extensions = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'zip', 'rar']
            extension = file.name.split('.')[-1].lower()
            if extension not in allowed_extensions:
                raise forms.ValidationError("Unsupported file type. Allowed types are: PDF, Word, Image, and Archive files.")
        return file