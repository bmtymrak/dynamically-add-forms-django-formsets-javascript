from django.views.generic import TemplateView, ListView
from .forms import BirdFormSet
from .models import Bird
from django.urls import reverse_lazy
from django.shortcuts import redirect


class BirdListView(ListView):
    model = Bird
    template_name = "bird_list.html"


class BirdAddView(TemplateView):
    template_name = "add_bird.html"

    def get(self, *args, **kwargs):

        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'formset': formset})

    def post(self, *args, **kwargs):

        formset = BirdFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("bird_list"))

        return self.render_to_response({'formset': formset})
