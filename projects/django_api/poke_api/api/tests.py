import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Pokemon, Trainers


class PokemonModelTest(TestCase):
    def test_was_published_recently_with_future_pokemon(self):
        """_summary_
            was_published_recently() returns False for pokemons whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_pokemon = Pokemon(pub_date=time)
        self.assertIs(future_pokemon.was_published_recently(), False)
