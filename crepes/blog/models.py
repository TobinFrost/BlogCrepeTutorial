#coding=utf-8
from django.db import models
import random
import string

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie')
    nb_vue = models.IntegerField(verbose_name='Nombre de Vue')

    def __str__(self):
        return self.titre

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    """ Modèle pour les commentaires. A vous de l'écrire ! """

class MiniURL(models.Model):
    url = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_acces = models.IntegerField(default=0,
                                   verbose_name="Nombre d'accès à l'URL")

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        self.code = ''.join(aleatoire)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"

class Personne(models.Model):
    nom = models.CharField(max_length=50,verbose_name="Nom")
    prenom =  models.CharField(max_length=60,verbose_name="Prenom")
    nb_modif = models.IntegerField(verbose_name="Nombre de Modification",null=True)

    def __unicode__(self):
        return u"[{0}] {1}".format(self.prenom, self.nom)