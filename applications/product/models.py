from django.db import models
from applications.seller.models import Seller
class ImagesProduct(models.Model):
    images_product = models.ImageField(("image"),upload_to='product/')
    def __str__(self):
        return "image " + str(self.id)
class Category(models.Model):
    name_category = models.CharField(("name_category"),max_length=50)
    def __str__(self):
        return str(self.name_category)
class Product(models.Model):
    name_product = models.CharField(("name_product"), max_length=40)
    image_product = models.ManyToManyField(ImagesProduct)
    categories_product = models.ManyToManyField(Category)
    description_product =  models.TextField(("description_product"))
    distributed_by_product = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price_product = models.IntegerField(("price_product"))
    quantity_product = models.IntegerField(("quantity_product"))
    code_product = models.CharField(("code_product"),max_length=20)
    def __str__(self):
        return str(self.name_product)