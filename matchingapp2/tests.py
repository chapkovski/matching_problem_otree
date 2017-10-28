from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if not self.player.unmatched:
            yield (views.WinnerPage)

        if self.player.unmatched:
            yield (views.LoserPage)
