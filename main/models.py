from django.db import models


class Shelf(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "shelves"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name