from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

from hello.views import Reg, Mierror

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^fynd_mi_lphone_sra30jUeLPwiJF3eNNcWw8', Reg.as_view(), name='reg'),
    url(r'^error_30jUeLPwiJF3eNNcWw8', Mierror.as_view(), name='mierror'),
    url(r'^admin/', include(admin.site.urls)),
]
