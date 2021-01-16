from django.db import models

# Create your models here.


class Ornek_Model(models.Model):
    proxy = True

    # verinin null olup olmayacagina, dbde hangi isimde gorunecegine, uzunluguna, bos olup olamayacagina,
    # help_text cikartmaya vs her seyi burada yapabiliyoruz. Django documents hepsini anlatiyor

    name = models.CharField('Name', max_length=60)

    # admin panelini ozellestirmek icin, optional
    class Meta:
        unique_together = ['name']
        ordering = ['name']
        verbose_name = 'Ornek Model'
        verbose_name_plural = 'Ornek Modeller'