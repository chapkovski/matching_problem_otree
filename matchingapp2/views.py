from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class FirstWP(WaitPage):
    group_by_arrival_time = True
    def get_players_for_group(self, waiting_players):
        true_players = [p for p in waiting_players if p.participant.vars.get('filter')]
        false_players = [p for p in waiting_players if not p.participant.vars.get('filter')]
        if len(true_players) >= 1 and len(false_players) >= 1:
            passers = true_players[:1] + false_players[:1]
            for p in passers:
                p.in_wp = False
                p.unmatched = False
                p.wp_passed = True
                p.save()
            return passers
        if self.session.mturk_num_participants != -1:
            num_participants = self.session.mturk_num_participants
        else:
            num_participants = len(self.session.get_participants())
        answered = [p for p in self.session.get_participants() if p.vars.get('filter') != None]
        left = num_participants - len(answered)
        over = len(waiting_players) - left
        if over > 0:
            losers = waiting_players[:over]
            for l in losers:
                l.unmatched = True
            return losers

class LoserPage(Page):
    def is_displayed(self):
        return self.player.unmatched


class WinnerPage(Page):
    def is_displayed(self):
        return not self.player.unmatched



page_sequence = [
    FirstWP,
    WinnerPage,
    LoserPage
]
