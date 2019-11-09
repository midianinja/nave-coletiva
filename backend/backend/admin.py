from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class NaveAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Nave Coletiva')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Nave Coletiva')

admin_site = NaveAdminSite()
