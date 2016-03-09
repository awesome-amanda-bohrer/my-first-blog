from django import forms

class UploadForm(forms.Form):
    upload = forms.FileField(label='Select a file')

class UploadForm2(forms.Form):
    upload2 = forms.FileField(label='Select a file')