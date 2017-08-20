from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from accounts import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.UserRegistrationView.as_view(), name='signup'),
    url(r'^profile/(?P<slug>[\w-]+)/$', views.UserProfileUpdate.as_view(), name='profile'),
    url(r'^users/$', views.listeRegisteredUser, name='users_list'),

]