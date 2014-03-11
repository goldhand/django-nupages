from django.views import generic

from .models import Page


class PageList(generic.ListView):
    model = Page
    paginate_by = 10


class PageDetail(generic.DetailView):
    model = Page