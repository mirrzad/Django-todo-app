import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Task


class Command(BaseCommand):
    help = "Create dummy tasks"

    def __init__(self, *args, **kwargs):
        self.fake = Faker()
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        user = User.objects.create(username=self.fake.name(), password='test123456789')
        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                is_completed=random.choice([True, False])
            )
