from django.views.generic import TemplateView, ListView, View
from .forms import BirdFormSet
from .models import Bird
from django.urls import reverse_lazy
from django.shortcuts import redirect

class BirdAddView(TemplateView):
    template_name = "add_bird.html"
    
    def get(self, *args, **kwargs):
        formset=BirdFormSet(queryset=Bird.objects.none())
        birds = Bird.objects.all()
        return self.render_to_response({'formset':formset, 'birds':birds})

    def post(self, *args, **kwargs):
        formset = BirdFormSet(data=self.request.POST)
        birds = Bird.objects.all()
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("add_bird"))

        return self.render_to_response({'formset': formset, 'birds':birds})


class BirdListView(ListView):
    model = Bird
    template_name="bird_list.html"