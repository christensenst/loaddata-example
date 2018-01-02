from django.db import models


class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


class Person(models.Model):
    objects = PersonManager()

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def natural_key(self):
        return self.first_name, self.last_name


class Office(models.Model):
    title = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
