from django.conf.urls import include, url
from blog import views
#from django.views.generic import ListView
#from .models import Article
urlpatterns = [
    #url(r'^$', views.accueil, name='accueil'),
    #url(r'^$',ListView.as_view(model=Article,template_name='blog/accueil.html')),
    url(r'^$', views.ListeArticleView.as_view(), name='blog_liste'),
    url(r'^categorie/(?P<id>\d+)$', views.ListeArticleByCategorieView.as_view(), name='blog_categorie'),
    #url(r'^(?P<slug>.+)$',views.lire_article, name='blog_lire'),
    url(r'^article/(?P<pk>\d+)$', views.LireArticleView.as_view(), name='details_article'),
    url(r'^personne/nouveau$', views.PersonneCreate.as_view(), name='nouveau_personne'),
    url(r'^personne/liste', views.liste_personne, name='liste_personne'),
    url(r'^personne/modify/(?P<pk>\d+)$', views.PersonneUpdate.as_view(), name='update_personne'),
    url(r'^personne/detail/(?P<pk>\d+)$', views.PersonneDetailView.as_view(), name='detail_personne'),
    url(r'^personne/delete/(?P<pk>\d+)$', views.PersonneDelete.as_view(), name='supprimer_personne'),
    url(r'^article/populaire$', views.ListeArticlePlusPopulaire.as_view(), name='article_populaire'),


]
