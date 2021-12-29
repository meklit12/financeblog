from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator
<<<<<<< HEAD

content_validator = MinLengthValidator(limit_value=300, message="Content should be atleast 300 characters long!")

=======
content_validator = MinLengthValidator(limit_value=300, message="Content should be atleast 300 characters long!")


>>>>>>> 30c7d3d263f020e02fa82aeeba7f2e4c7a4ec528
class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[content_validator])
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})
=======
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})


>>>>>>> 30c7d3d263f020e02fa82aeeba7f2e4c7a4ec528
