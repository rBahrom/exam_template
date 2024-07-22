from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

class Shop(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='shop/picture/')
    descriptions = models.TextField()
    miqdor = models.PositiveIntegerField(default=0, null=True)
    count = models.PositiveIntegerField(default=0, null=True)
    price = models.FloatField()
    reyting = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.category}"
                f"{self.descriptions}"
                f"{self.price}"
                f"{self.count}"
                f"{self.miqdor}")

