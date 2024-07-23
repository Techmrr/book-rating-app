from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from postgresTest.models import Book, Review

class Command(BaseCommand):
    help = 'Load data from database.txt'

    def handle(self, *args, **kwargs):
        # Load data from database.txt
        with open('./database.txt', 'r') as file:
            lines = file.readlines()

        # Variables to store data
        book_lines = []
        user_lines = []
        review_lines = []

        # Parse the lines into respective categories
        for line in lines:
            if line.startswith('INSERT INTO books'):
                book_lines.append(line)
            elif line.startswith('INSERT INTO users'):
                user_lines.append(line)
            elif line.startswith('INSERT INTO reviews'):
                review_lines.append(line)

        # Create Books
        for line in book_lines:
            data = line.split('VALUES')[1].strip().strip('();').split('),(')
            for record in data:
                title, author, genre = record.split(',')
                Book.objects.get_or_create(
                    title=title.strip("' "),
                    author=author.strip("' "),
                    genre=genre.strip("' ")
                )

        # Create Users
        for line in user_lines:
            data = line.split('VALUES')[1].strip().strip('();').split('),(')
            for record in data:
                username, password = record.split(',')
                User.objects.get_or_create(
                    username=username.strip("' "),
                    defaults={'password': password.strip("' ")}
                )

        # Create Reviews
        for line in review_lines:
            data = line.split('VALUES')[1].strip().strip('();').split('),(')
            for record in data:
                book_id, user_id, rating = record.split(',')
                Review.objects.get_or_create(
                    book_id=book_id.strip(),
                    user_id=user_id.strip(),
                    rating=rating.strip()
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
