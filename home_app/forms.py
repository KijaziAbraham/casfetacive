from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)



from .models import AboutUsContent

class AboutUsContentForm(forms.ModelForm):
    class Meta:
        model = AboutUsContent
        fields = '__all__'
