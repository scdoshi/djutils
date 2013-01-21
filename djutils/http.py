"""
HTTP: HTTP related utilities.

"""

###############################################################################
## Imports
###############################################################################
from django.contrib.sites.models import Site
from django.http import HttpResponse


###############################################################################
## Responses
###############################################################################
class HttpResponseNotAuthorized(HttpResponse):
    """Not Authorized 401 response to use HTTP Basic Auth with django"""
    status_code = 401

    def __init__(self, redirect_to):
        HttpResponse.__init__(self)
        self['WWW-Authenticate'] = ('Basic realm="%s"' %
            Site.objects.get_current().name)
