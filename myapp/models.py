from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=120)

    last_name = models.CharField(max_length=120)

    email = models.CharField(max_length=120)

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=120)

    city = models.CharField(max_length=120)

    state = models.CharField(max_length=120)

    country = models.CharField(max_length=120)



    def __str__(self):

        return self.first_name + "   " + self.last_name


