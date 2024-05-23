from django.db import models
from django.urls import reverse

class Course(models.Model):
    slug = models.SlugField() # Для создания своего URL адреса
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})
    
    

