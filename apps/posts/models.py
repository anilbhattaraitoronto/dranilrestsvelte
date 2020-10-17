# dependencies for creating thumbnails
from io import BytesIO
from django.core.files import File
from PIL import Image


from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    image = models.ImageField(blank=True, null=True, upload_to='tags/')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    image = models.ImageField(blank=True, null=True, upload_to='categories/')
    ordering = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['ordering']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    featured = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(blank=True, null=True, upload_to='posts/images/')
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="posts/thumbnails/")
    imageurl = models.URLField(max_length=255, blank=True, null=True)
    summary = models.TextField()
    content = RichTextUploadingField()
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_date', 'category']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(150, 120)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thum_io = BytesIO()
        img.save(thum_io, 'JPEG', quality=85)
        thumbnail = File(thum_io, name=image.name)
        return thumbnail
