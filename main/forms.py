from django.forms import ModelForm
from .models import Poll

#creating a form for the "create" page.
class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']