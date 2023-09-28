from django.db import models


class Apartment(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)  # Convert number to string before returning


class Resident(models.Model):
    name = models.CharField(max_length=100)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='resident_apartment')

    def __str__(self):
        return self.name


class Post(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='post_resident')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
