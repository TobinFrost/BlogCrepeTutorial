from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^faq/',TemplateView.as_view(template_name='blog/faq.html')),

]