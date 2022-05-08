from turtle import width
from django import forms
from .models import BlogComment, Contact, Blog
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ("first_name", "last_name", "e_mail")
        # exclude = ("first_name",)

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'})
        }

class CreateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }

class UpdateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }
        

class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = "__all__"
        
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'blog': forms.TextInput(attrs={'value': '', 'id':'blog', 'type':'hidden'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }