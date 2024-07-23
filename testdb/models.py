from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)

    class Meta:
        unique_together = ('title', 'author', 'genre')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='testdb_reviews')
    rating = models.PositiveIntegerField()

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
