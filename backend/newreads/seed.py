from django.core.management.base import BaseCommand
from library.open_library import get_or_create_book
from userprofile.models import BookList, User


class Command(BaseCommand):
    help = "Seed the database with books and users"

    def handle(self, *args, **kwargs):
        self.seed_books()
        self.seed_users_and_lists()

    def seed_books(self):
        default_books = [
            "OL7353617M",  # The Hobbit
            "OL1234567M",
            "OL2468101M",
        ]

        for ol_id in default_books:
            try:
                book = get_or_create_book(ol_id)
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Seeded book: {book.title} by {book.author_name}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"❌ Failed to seed book with OL ID {ol_id}: {e}")
                )

    def seed_users_and_lists(self):
        default_users = [
            {"username": "user1", "email": "user1@example.com", "password": "password123"},
            {"username": "user2", "email": "user2@example.com", "password": "password123"},
        ]

        for user_data in default_users:
            user, created = User.objects.get_or_create(
                username=user_data["username"], defaults={"email": user_data["email"]}
            )
            if created:
                user.set_password(user_data["password"])
                user.save()
                self.stdout.write(self.style.SUCCESS(f"👤 Created user: {user.username}"))
            else:
                self.stdout.write(f"ℹ️ User already exists: {user.username}")

            # Create default book list if not exists
            if not BookList.objects.filter(user=user, name="Default Book List").exists():
                BookList.objects.create(
                    user=user,
                    name="Default Book List",
                    description="A list of favorite books.",
                    is_public=True,
                )
                self.stdout.write(self.style.SUCCESS(f"📚 Created book list for {user.username}"))
