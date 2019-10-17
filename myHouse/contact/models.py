from django.db import models

# Create your models here.

class Message(models.Model):
    # TODO: Define fields here
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return '{}'.format(self.nom)


class Newsletter(models.Model):
    # TODO: Define fields here
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email

class Apel(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
