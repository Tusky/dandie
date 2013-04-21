from django.forms import ModelForm
from news.models import New


class NewForm(ModelForm):
    class Meta:
        model = New
