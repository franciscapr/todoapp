from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:    # Definimos los metadatos para la base de datos
        model = Todo    # Especificamos el modelo en el que se basara el formulario
        fields = '__all__'    # Especificamos los campos que se incluiran en el form en este caso __all__ es todos
        
        label = {    # Proporcionamos las etiquetas en los campos del form
            'title': 'Title',
            'description': 'Description',
        }
        
        widgets = {    # Personaliza los widgets HTML para los campos del form agregando marcadores de posición
            'title': forms.TextInput(attrs={'placeholder':'Buy Groceries'}),
            'description': forms.TextInput(attrs={'placeholder': 'Visit super market and buy some groceries'}),
        }