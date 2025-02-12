from django.db import models

class Image2(models.Model):
    file = models.ImageField(upload_to='images2/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Изображение {self.id}"
