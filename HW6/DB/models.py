from django.db import models

# Create your models here.
class Maker (models.Model): 
    name = models.CharField(max_length = 10)
    country = models.CharField(max_length = 10)

    def __str__ (self) -> str: return self.name

class PModel (models.Model): 
    maker = models.ForeignKey(Maker, on_delete = models.SET_DEFAULT, default = 1)
    name = models.CharField(max_length = 20)
    url = models.URLField(default = 'http://i.imgur.com/Ous4iGB.png')

    def __str__ (self) -> str: return self.name

class Product (models.Model): 
    pmodel = models.ForeignKey(PModel, on_delete = models.SET_DEFAULT, default = 1, verbose_name = '型號')
    # pmodel = models.ForeignKey(PModel, on_delete = models.CASCADE, verbose_name = '型號')
    nickname = models.CharField(max_length = 115, default = '超值手機')
    description = models.TextField(default = '暫無說明')
    year = models.PositiveIntegerField(default = 2024)
    price = models.PositiveIntegerField(default = 0)

    def __str__ (self) -> str : return self.nickname

class PPhoto (models.Model): 
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    description = models.CharField(max_length = 20, default = '產品照片')
    url = models.URLField(default = 'http://i.imgur.com/Z230eeq.png')

    def __str__ (self) -> str: return self.description




























