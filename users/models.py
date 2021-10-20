from django.db import models
from django.utils import timezone

# Create your models here.
# Profile model


class Feedback(models.Model):

    first_name = models.CharField(
        verbose_name="First Name", max_length=254, blank=True)
    last_name = models.CharField(
        verbose_name="Last Name", max_length=254, blank=True)
    ticket = models.IntegerField()

    person = models.CharField(verbose_name="Person",
                              max_length=254, blank=True)

    email = models.EmailField(max_length=254)
    message = models.CharField(verbose_name="Message", max_length=254)
    isTechnical = models.BooleanField(default=False)

    date = models.DateField(default=timezone.now)
    wasSeen = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.first_name.capitalize()}' + ' ' + f'{self.last_name.capitalize()}' + ' ➜ ' + f'{self.person}'
    
    class Meta:
         verbose_name = 'Feedback'
         verbose_name_plural = "Feedback"
        


class Announcement(models.Model):

    title = models.CharField(verbose_name="Title", max_length=254, blank=True)
    message = models.TextField(verbose_name='Message', max_length=10000)
    date = models.DateField(default=timezone.now)
    announcementID = models.IntegerField()

    def __str__(self):
        return f'{self.title.capitalize()}'

    class Meta:
         verbose_name = "Announcement"
         verbose_name_plural = "Announcements"

class Dates(models.Model):
    
    title = models.CharField(verbose_name="Title", max_length=254)
    dates = models.TextField(verbose_name='Message', max_length=5000)
    

    def __str__(self):
        return f'{self.title}'

    class Meta:
         verbose_name = "Date"
         verbose_name_plural = "Dates"

class Inductees(models.Model):
    
    year = models.IntegerField(verbose_name="Year")
    inductees = models.TextField(verbose_name='Message', max_length=2000)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.year}'

    class Meta:
         verbose_name = "List of Inductees"
         verbose_name_plural = "Inductees"

class Officers(models.Model):
    
    
    name = models.CharField(verbose_name="Name", max_length=254, blank=True)
    position = models.TextField(verbose_name='Position', max_length=254)
    isBig = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
         verbose_name = "List of Officers"
         verbose_name_plural = "Officers"

