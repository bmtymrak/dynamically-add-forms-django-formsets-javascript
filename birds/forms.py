from django.forms import modelformset_factory
from .models import Bird

BirdFormSet = modelformset_factory(Bird, fields=('common_name', 'scientific_name'), extra = 2)