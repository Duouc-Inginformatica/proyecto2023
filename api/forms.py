from msilib.schema import Class # pylint: disable=import-error
from django import forms #importar libreria forms
from api.models import Sebe #importar tabla maule

class SebeForm(forms.ModelForm): #crear clase MauleForm
    class Meta: #crear clase Meta
        model = Sebe #crear modelo Maule
        fields = ['tipo', 'nombre', 'descripcion', 'precio', 'imga', 'imgb', 'descuento'] #crear campos