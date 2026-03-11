from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='carousel/')
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers display first.")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="e.g., 'fas fa-book'. Use Font Awesome class names.")
    description = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

class LiveClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    link = models.URLField()

    class Meta:
        ordering = ['date']
        verbose_name = "Live Class"
        verbose_name_plural = "Live Classes"

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage featured section.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ['-date'] # Show most recent first

    def __str__(self):
        return self.title 