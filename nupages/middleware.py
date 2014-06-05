from django.contrib.sites.models import Site
from django.conf import settings


class MultiTenantMiddleware(object):
    '''
    Adds site_id to requests for multitenancy
    '''
    def process_request(self, request):
        ''' 
        checks if the host domain is one of the site objects
        and sets request.site_id
        '''
        site_id = 0
        domain = request.get_host().lower()
        if hasattr(settings, 'SITE_ID'):
            site_id = settings.SITE_ID
        try:
            site = Site.objects.get(domain__iexact=domain)
            site_id = site.id
        except Site.DoesNotExist:
            pass
        request.site_id = site_id