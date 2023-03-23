from django.db import models

# Create your models here.
class Nout(models.Model):

    name = models.CharField('Nout name', max_length=50)
    img = models.ImageField('Nout image', upload_to='images')
    price = models.IntegerField('Nout price')
    about = models.TextField('Nout about')
    date = models.DateTimeField('Nout create date', auto_now=True)
    slug = models.SlugField('Nout slug', unique=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Nout'
        verbose_name_plural = 'Nouts'
        ordering = ['date']
    