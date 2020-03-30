from django.db import models

# Create your models here.
class Product(models.Model):
    category = (('dishwashing','Dishwashing'), ('laundry', 'Laundry'), ('cleaning', 'Cleaning'), ('disinfection', 'Disinfection'), ('body care', 'Body Care'), ('other', 'Other'))
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=15, choices=category, default='')

    def __str__(self):
        return self.name

class product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True)
    

def __str__(self):
    return self.product.name+ ': ' + str(self.id)