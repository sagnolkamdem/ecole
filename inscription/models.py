from django.db import models


# Create your models here.


class profile(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.IntegerField()
    quat = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Serie(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Eleve(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.IntegerField()
    quat = models.CharField(max_length=100)
    datenaiss = models.DateTimeField()

    def __str__(self):
        return self.nom


class Classe(models.Model):
    libelle = models.CharField(max_length=100)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle


class Intendant(models.Model):
    nom = models.CharField(max_length=140)
    prenom = models.CharField(max_length=100)
    tel = models.IntegerField()
    quat = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Inscription(models.Model):
    date_ins = models.DateTimeField(auto_now_add=True)
    validation = models.BooleanField(default=False)
    annee_academique = models.CharField(max_length=100, default='2021-2022')
    utilisateur = models.ForeignKey(profile, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    intendant = models.ForeignKey(Intendant, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_ins +" "+ self.eleve

class Article(models.Model):
    nom=models.CharField(max_length=100)