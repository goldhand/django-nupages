from django.views import generic
from django.template.loader import select_template
from django.shortcuts import render

from .models import Page


def home_page(request):
    page_base_template_names = ["nupages/base.html",]
    page_template_names = ["nupages/index.html",]
    page_list = Page.objects.published()
    page = None
    context = {}
    if hasattr(request, 'site_id'):
        # filter page_list by active site_id
        page_list = page_list.filter(site_id=request.site_id)
        # use site's base template if it exists
        page_base_template_names.insert(0, 
            "nupages/tenants/{}/base.html".format(request.site_id))

        # use site's index.html instead of default nupages index if it exists
        page_template_names.insert(0, 
            "nupages/tenants/{}/index.html".format(request.site_id))
        try:
            page = Page.objects.published().get(site_id=request.site_id, 
            slug__istartswith='home')

        except Page.DoesNotExist:
            print 'Does not exist'
            
        except Page.MultipleObjectsReturned:
            print 'multiple'

    if page:
        context['page'] = page
        # use a custom template if specified
        if page.custom_template:
            page_template_names.insert(0, page.custom_template)

    context['page_list'] = page_list
    # select correct base template
    page_base_template = select_template(page_base_template_names)
    context['base_template'] = page_base_template

    return render(request, page_template_names, context)



class PageList(generic.ListView):
    model = Page
    queryset = Page.objects.published()
    paginate_by = 10

    def get_queryset(self):
        '''
        If MultiTenantMiddleware is used, filter queryset by request.site_id
        '''
        queryset = super(PageList, self).get_queryset()
        if hasattr(self.request, 'site_id'):
            queryset = queryset.filter(site_id=self.request.site_id)
        return queryset

    def get_context_data(self, **kwargs):
        '''
        Adds a 'base_template' attribute to context for the page_detail to 
        extend from
        '''
        context = super(PageList, self).get_context_data(**kwargs)
        page_base_template = "nupages/base.html"
        # if MultiTenantMiddleware is used, use a base template specific to 
        # the tenants SITE_ID
        if hasattr(self.request, 'site_id'):
            page_base_template = select_template(
                ["nupages/tenants/{}/base.html".format(self.request.site_id), 
                page_base_template])
        context['base_template'] = page_base_template
        print page_base_template
        return context



class PageDetail(generic.DetailView):
    model = Page
    template_name = 'nupages/page_detail.html'
    queryset = Page.objects.published()

    def get_template_names(self):
        '''
        Looks for a custom_template value and prepends it to template_names 
        if it exists otherwise 'nupages/page_detail.html' is used
        '''
        template_names = super(PageDetail, self).get_template_names()
        if self.get_object().custom_template:
            # there is a custom template, insert it before 'template_name'
            template_names.insert(0, self.get_object().custom_template)
        return template_names

    def get_queryset(self):
        '''
        If MultiTenantMiddleware is used, filter queryset by request.site_id
        '''
        queryset = super(PageDetail, self).get_queryset()
        if hasattr(self.request, 'site_id'):
            queryset = queryset.filter(site_id=self.request.site_id)
        return queryset

    def get_context_data(self, **kwargs):
        '''
        Adds a 'base_template' attribute to context for the page_detail to 
        extend from
        '''
        context = super(PageDetail, self).get_context_data(**kwargs)
        page_base_template = "nupages/base.html"
        # if MultiTenantMiddleware is used, use a base template specific to 
        # the tenants SITE_ID
        if hasattr(self.request, 'site_id'):
            page_base_template = select_template(
                ["nupages/tenants/{}/base.html".format(self.request.site_id), 
                page_base_template])
        context['base_template'] = page_base_template
        return context
