from django.core.management.base import BaseCommand
from api.models import User,ActivityPeriod
# import UserFactory here
import factory  
import factory.django

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = User

    real_name = factory.Faker('name')
    tz = factory.Faker('address')


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=10,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            user1=UserFactory.create()
            ActivityPeriod.objects.create(user=user1,start_time='mar 2 10 2:30AM',start_time='apr 1 11 2:30AM',)