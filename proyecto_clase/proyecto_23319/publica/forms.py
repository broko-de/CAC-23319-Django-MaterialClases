from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email',max_length=50)
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(label='Mensaje')