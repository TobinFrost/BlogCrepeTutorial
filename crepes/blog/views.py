#coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Article,Categorie,MiniURL,Personne
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import MiniURLForm,PersonneForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q,Max
def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)

    return render(request, 'blog/lire_article.html', {'article': article})

class ListeArticleView(ListView):
    model = Article #Le modele à Lister
    context_object_name = 'derniers_articles' # la variable qui recupere la liste des article
    template_name = 'blog/reaccueil.html' # le template qui sera afficher et rediriger
    paginate_by = 5 # on pagine pas 5
    #queryset = Article.objects.filter(categorie__id=1)

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticleView, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context

class ListeArticleByCategorieView(ListView):
    model = Article #Le modele à Lister
    context_object_name = 'derniers_articles' # la variable qui est renvoyés au template
    template_name = 'blog/reaccueil.html' # le template qui sera afficher et rediriger
    paginate_by = 5 # on pagine pas 5
    #queryset = Article.objects.filter(categorie__id=1)
    def get_queryset(self):
        #return Article.objects.filter(categorie_id=self.args[0])
        #return Article.objects.filter(categorie_id=self.kwargs['id'])
        return Article.objects.annotate()


class ListeArticlePlusPopulaire(ListView):
    model = Article
    context_object_name = 'articles_populaire'
    template_name = 'blog/article_populaire.html'

    def get_queryset(self):
        critere = 1
        #return Article.objects.filter(Q(nb_vue__gte=critere))
        return  Article.objects.filter().aggregate(Max('nb_vue'))

class LireArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/relire_article.html'

    # def get_queryset(self): # cette methode n'est pas bonne
    #     # Nous récupérons l'objet, via la super-classe
    #     article = super(LireArticleView, self).get_object()
    #     article.nb_vue += 1
    #     article.save()
    #     return article # Et nous retournons l'objet à afficher

    def get_object(self):
        article = super(LireArticleView, self).get_object()
        article.nb_vue +=1
        article.save()
        return article


class PersonneDetailView(DetailView):
    model = Personne
    context_object_name = 'personne'
    template_name = 'personne/detail.html'


def liste_personne(request):
    personnes = Personne.objects.order_by("nom")
    return render(request, 'personne/liste.html', locals())


class PersonneCreate(CreateView):
    model = Personne
    template_name = 'personne/nouveau.html'
    form_class = PersonneForm
    success_url = reverse_lazy(liste_personne)


class PersonneUpdate(UpdateView):
    model = Personne
    template_name = 'personne/nouveau.html'
    form_class = PersonneForm
    success_url = reverse_lazy(liste_personne)

    # def get_object(self):
    #     personne = super(PersonneUpdate,self).get_object()
    #     personne.nb_modif += 1
    #     personne.save()
    #     return personne
    def form_valid(self, form):
        self.object = form.save()
        personne = super(PersonneUpdate, self).get_object()
        increment = 1
        personne.nb_modif += increment
        personne.save()

        messages.success(self.request, "Votre profil a été mis à jour avec succès.", extra_tags="alert-warning alert")
        return HttpResponseRedirect(self.get_success_url())

class PersonneDelete(DeleteView):
    model = Personne
    template_name = 'personne/supprimer.html'
    context_object_name = 'personne'
    success_url = reverse_lazy(liste_personne)

