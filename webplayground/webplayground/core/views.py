from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render



class HomePageView(TemplateView):
    
    template_name = "core/home.html"
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['title'] = 'Mi super wev'
        #return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'mi ew'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"