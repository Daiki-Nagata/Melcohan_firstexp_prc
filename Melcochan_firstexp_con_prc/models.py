from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'Melcochan_firstexp_con_prc'
    players_per_group = None
    num_rounds = 2

    instructions_template = 'Melcochan_firstexp_con_prc/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    check_1 = models.IntegerField(
        label='', min=0, max=10)

    check_2 = models.IntegerField(
        label='', min=0, max=10)

    prc_adv = models.IntegerField(
        label='', 
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )

    prc_quality = models.IntegerField(
        label='',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    
class Cal():
    player = models.Link(Player)

    prev_player = player.in_round(self.round_number - 1)
    print(prev_player)

    """while True:
        if num_rounds == 1:
            Sales1 = models.IntegerField(
            prc_adv^0.35*prc_quality^0.7*10      
        )
        else:
            Sales = prc_adv^0.35*prc_quality^0.35*Prc_quality^0.35*10 

    sales1 = models.IntegerField(
        prc_adv^0.35*prc_quality^0.7*10      
    ) """
