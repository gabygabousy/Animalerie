from django.db import models
from django.shortcuts import get_object_or_404
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip
 
 
class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_animal

def lit_race(id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    animaux = Animal.objects.all()
    if animal in animaux :
        return animal.race


def lit_état(id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    animaux = Animal.objects.all()
    if animal in animaux :
        return animal.etat

def lit_lieu(id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    animaux = Animal.objects.all()
    if animal in animaux :
        return animal.lieu

def vérifie_disponibilité(id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    equipements = Equipement.objects.all()
    if equipement in equipements:
        return equipement.disponibilite

def cherche_occupant(lieu):
    equipements = Equipement.objects.all()
    animaux = Animal.objects.all()
    Lieu = get_object_or_404(Equipement, id_equip=lieu)
    if Lieu in equipements:
        liste_animal = []
        for animal in animaux:
            if animal.lieu == Lieu:
                liste_animal.append(animal.id_animal)
        return ( liste_animal)


def change_état(id_animal, état):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    animaux = Animal.objects.all()
    if animal in animaux:
        if état in ['affamé','fatigué', 'repus','endormi']:
            animal.etat = état
            animal.save()

def change_lieu(id_animal, lieu):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    Lieu = get_object_or_404(Equipement, id_equip=lieu)
    equipements = Equipement.objects.all()
    animaux = Animal.objects.all()
    if Lieu in equipements and animal in animaux:
        ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        if Lieu.id_equip == 'Litière':
            ancien_lieu.disponibilite = 'libre'
            ancien_lieu.save() 
            animal.lieu = Lieu
            animal.save() 
        elif Lieu.id_equip != 'Litière' and  Lieu.disponibilite == 'libre' :
            ancien_lieu.disponibilite = 'libre'
            ancien_lieu.save()              
            animal.lieu = Lieu
            animal.save()
            Lieu.disponibilite = 'occupé'
            Lieu.save() 
        else:
            pass