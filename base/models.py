from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.category_name)

class Doctors(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    doc_name=models.CharField(max_length=100)
    Institute=models.CharField(max_length=100)
    fee=models.CharField(max_length=10)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.doc_name)
