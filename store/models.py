
from django.db import models
from django.urls import reverse
from django.utils import timezone
from shop.settings import AUTH_USER_MODEL


class category(models.Model):
    name = models.CharField(max_length=128)
    date_ajout = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="product", blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category, related_name='categorie', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_ajout']


    def __str__(self):
        return f"{self.name} ({self.stock})"


    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    

class Publicite(models.Model):
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)    
    thumbnail = models.ImageField(upload_to="product", blank=True, null=True)

class order(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} ({self.product.name}) ({self.quantity})"
    
    def sous_total(self):
        return((self.quantity) * (self.product.price))


class cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(order)


    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for Order in self.orders.all():
            Order.ordered = True
            Order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)



class command(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    Cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    email = models.EmailField()
    Address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pays = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    Total_command = models.IntegerField(default=0)
    Nbre_Article = models.IntegerField(default=0)
    date_command = models.DateTimeField(blank=True, null=True)

    def __str__(self):
       return f"{self.user}"



class Article(models.Model):
    Command = models.ForeignKey(command, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    quantite = models.IntegerField(default=0)


    def __str__(self):
        return self.name
