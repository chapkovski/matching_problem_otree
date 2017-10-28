from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_fields = ['mychoice']
    form_model = models.Player
    def before_next_page(self):
        self.participant.vars['filter']=self.player.mychoice




page_sequence = [
    MyPage,
]
