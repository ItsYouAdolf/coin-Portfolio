from django.shortcuts import render
from django.views.generic.base import View
from .models import description
from django.views.generic import DetailView

# Create your views here.


class CoinsManager(View):
    def get(self, reguest):
        coinsmanager = description.objects.all()
        return render(reguest, 'osnova/prosto.html', {'posts': coinsmanager,})

class strdin(DetailView):
    model = description
    template_name = 'osnova/suk.html'
    context_object_name = 'Post'

