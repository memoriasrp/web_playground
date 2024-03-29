from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy
# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        #if not request.user.is_staff:
        #    return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model =Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url= reverse_lazy('pages:pages')

    
class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    #success_url= reverse_lazy('pages:pages')
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id])+'?ok'

class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page

    success_url = reverse_lazy('pages:pages')