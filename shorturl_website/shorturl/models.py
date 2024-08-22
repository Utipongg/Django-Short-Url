from django.db import models

# Create your models here.
class UrlDb(models.Model):
    code = models.TextField(max_length=10, unique=True, blank=True)
    longurl = models.URLField()

    def __str__(self):
        return self.long_longurlurl

    def save(self, *args, **kwargs):
        if not self.code:
            self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):

        import string
        import random

        while True:
            code = ''.join(random.choice(string.ascii_letters) for _ in range(6))
            if not UrlDb.objects.filter(code=code).exists():
                self.code = code
                break