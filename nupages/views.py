from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Page, Tag


class PageList(generic.ListView):
	model = Page
	queryset = Page.objects.published()
	paginate_by = 10
	template_name = "nupages/list.html"

	def get_queryset(self):
		queryset = super(PageList, self).get_queryset()
		if not self.request.user.is_authenticated():
			queryset = queryset.filter(public=True)
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(PageList, self).get_context_data(*args, **kwargs)
		context['tags'] = Tag.objects.all()
		return context


class PageDetail(generic.DetailView):
	model = Page
	template_name = "nupages/detail.html"

	def get_context_data(self, **kwargs):
		context = super(PageDetail, self).get_context_data(**kwargs)
		if context['page'].custom_template:
			self.template_name = "nupages/%s.html" % context['page'].slug
		context['tags'] = Tag.objects.all()
		return context


class PageFilter(generic.ListView):
	model = Page
	queryset = Page.objects.published()
	paginate_by = 10
	template_name = "nupages/list.html"

	def get_queryset(self):
		self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
		queryset = self.tag.page_set.published()
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(PageFilter, self).get_context_data(*args, **kwargs)
		context['tag'] = self.tag
		context['tags'] = Tag.objects.all()
		return context