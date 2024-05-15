# from django import forms

# class UsuarioForm(forms.Form):
#     nombre= forms.CharField(label="nombre", required=True)
#     apellido= forms.CharField(label="apellido", required=True)
#     dni= forms.IntegerField(label="dni", required=True)
#     email= forms.EmailField(label="email", required=True)


from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True) 
    apellido = forms.CharField(label="Apellido", required=True) 
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)
    direccion = forms.CharField(label="Direccion", required=True) 