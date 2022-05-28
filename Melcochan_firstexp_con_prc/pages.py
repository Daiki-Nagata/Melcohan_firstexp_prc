from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instraction(Page):
    pass

class Manucheck(Page):
    form_model = 'player'
    form_fields = ['check_1', 'check_2']
    def is_displayed(self):
        return self.round_number == 1

class Practice(Page):
    form_model = 'player'
    form_fields = ['prc_adv', 'prc_quality']
    @staticmethod
    def error_message(values):
        print('values is', values)
        if values['prc_adv'] + values['prc_quality'] != 10:
            return '合計が10となるように配分してください。'

class Result(Page):
    form_model = 'player'
    form_fields = ['prc_adv', 'prc_quality']

page_sequence = [Introduction, Manucheck, Practice, Result]
