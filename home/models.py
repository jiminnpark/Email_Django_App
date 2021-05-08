from django.db import models

# Create your models here.


class attachment(models.Model):
    fi = models.URLField(null=True, blank=True)
    app_label = 'email_app'
