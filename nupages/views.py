from django.views import generic

from .models import Page


class PageList(generic.ListView):
	model = Page
	queryset = Page.objects.published()
	paginate_by = 10


class PageDetail(generic.DetailView):
	model = Page

	def get_context_data(self, **kwargs):
		context = super(PageDetail, self).get_context_data(**kwargs)
		if context['page'].custom_template:
			self.template_name = "nupages/%s.html" % context['page'].slug
		return context