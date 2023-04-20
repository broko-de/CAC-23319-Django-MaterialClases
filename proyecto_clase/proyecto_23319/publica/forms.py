from django import forms

class ContactoForm(forms.Form):
    TIPO_CONSULTA = (
        ('','-Seleccione-'),
        (1,'Inscripciones'),
        (2,'Soporte del Aula Virtual'),
        (3,'Ser docente'),
    )

    nombre = forms.CharField(label='Nombre y Apellido',required=False)
    email = forms.EmailField(label='Email',max_length=50)    
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(label='Mensaje')
    # dni = forms.IntegerField(label='dni')
    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        initial=1
    )
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las novedades',
        required=False
    )