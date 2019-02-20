from random import random
import time
import json
import click


def json_dumps(object):
    print(json.dumps(object, indent=4))


class Card():
    def __init__(self, smallest_card, biggest_card):
        self.smallest_number = smallest_card
        self.biggest_number = biggest_card
        multiplicator = self.biggest_number - self.smallest_number
        self.value = round(random() * multiplicator + self.smallest_number)


class Player():
    def __init__(self, name, number_of_cards, smallest_card, biggest_card):
        self.cards = list()
        self.name = name
        for a in range(0, number_of_cards):
            self.cards.append(Card(smallest_card=smallest_card, biggest_card=biggest_card))

        self.run()

    def run(self):
        pass


class Human(Player):
    pass


class CPU(Player):
    def run(self):
        self.minimum_time = 2
        self.maximum_time = 4

    def answer_time(self):
        multiplicator = self.maximum_time - self.minimum_time
        return round(random() * multiplicator + self.minimum_time)


class Game():
    def __init__(self, player_name, number_of_cards, smallest_card, biggest_card, level):
        self.player = Human(
            name=player_name,
            number_of_cards=number_of_cards,
            smallest_card=smallest_card,
            biggest_card=biggest_card
        )

        self.computer = CPU(
            name="Computer",
            number_of_cards=number_of_cards,
            smallest_card=smallest_card,
            biggest_card=biggest_card
        )

        if level == "easy":
            self.computer.minimum_time = 4
            self.computer.maximum_time = 10
        if level == "normal":
            self.computer.minimum_time = 2
            self.computer.maximum_time = 6
        if level == "hard":
            self.computer.minimum_time = 2
            self.computer.maximum_time = 4
        if level == "nightmare":
            self.computer.minimum_time = 1
            self.computer.maximum_time = 3
        self.war_cards = list()
        self.draw = False
        self.war_banner = """
                                                    ,---,    ,---,    ,---,  
                                                  ,`--.' | ,`--.' | ,`--.' |  
           .---.   ,---,       ,-.----.           |   :  : |   :  : |   :  :  
          /. ./|  '  .' \      \    /  \          '   '  ; '   '  ; '   '  ;  
      .--'.  ' ; /  ;    '.    ;   :    \         |   |  | |   |  | |   |  |  
     /__./ \ : |:  :       \   |   | .\ :         '   :  ; '   :  ; '   :  ;  
 .--'.  '   \' .:  |   /\   \  .   : |: |         |   |  ' |   |  ' |   |  '  
/___/ \ |    ' '|  :  ' ;.   : |   |  \ :         '   :  | '   :  | '   :  |  
;   \  \;      :|  |  ;/  \   \|   : .  /         ;   |  ; ;   |  ; ;   |  ;  
 \   ;  `      |'  :  | \  \ ,';   | |  \         `---'. | `---'. | `---'. |  
  .   \    .\  ;|  |  '  '--'  |   | ;\  \         `--..`;  `--..`;  `--..`;  
   \   \   ' \ ||  :  :        :   ' | \.'        .--,_    .--,_    .--,_     
    :   '  |--" |  | ,'        :   : :-'          |    |`. |    |`. |    |`.  
     \   \ ;    `--''          |   |.'            `-- -`, ;`-- -`, ;`-- -`, ; 
      '---"                    `---'                '---`"   '---`"   '---`"  
                                                                              
        
        """
        self.win_banner = """


                                                ,---,    ,---,    ,---,  
                                 ,--.        ,`--.' | ,`--.' | ,`--.' |  
           .---.   ,---,       ,--.'|        |   :  : |   :  : |   :  :  
          /. ./|,`--.' |   ,--,:  : |        '   '  ; '   '  ; '   '  ;  
      .--'.  ' ;|   :  :,`--.'`|  ' :        |   |  | |   |  | |   |  |  
     /__./ \ : |:   |  '|   :  :  | |        '   :  ; '   :  ; '   :  ;  
 .--'.  '   \' .|   :  |:   |   \ | :        |   |  ' |   |  ' |   |  '  
/___/ \ |    ' ''   '  ;|   : '  '; |        '   :  | '   :  | '   :  |  
;   \  \;      :|   |  |'   ' ;.    ;        ;   |  ; ;   |  ; ;   |  ;  
 \   ;  `      |'   :  ;|   | | \   |        `---'. | `---'. | `---'. |  
  .   \    .\  ;|   |  ''   : |  ; .'         `--..`;  `--..`;  `--..`;  
   \   \   ' \ |'   :  ||   | '`--'          .--,_    .--,_    .--,_     
    :   '  |--" ;   |.' '   : |              |    |`. |    |`. |    |`.  
     \   \ ;    '---'   ;   |.'              `-- -`, ;`-- -`, ;`-- -`, ; 
      '---"             '---'                  '---`"   '---`"   '---`"  
                                                                         


"""

        self.lose_banner = """
                                                


   ,--,                                                 ,---,    ,---,    ,---,  
,---.'|       ,----..                                ,`--.' | ,`--.' | ,`--.' |  
|   | :      /   /   \   .--.--.       ,---,.        |   :  : |   :  : |   :  :  
:   : |     /   .     : /  /    '.   ,'  .' |        '   '  ; '   '  ; '   '  ;  
|   ' :    .   /   ;.  \  :  /`. / ,---.'   |        |   |  | |   |  | |   |  |  
;   ; '   .   ;   /  ` ;  |  |--`  |   |   .'        '   :  ; '   :  ; '   :  ;  
'   | |__ ;   |  ; \ ; |  :  ;_    :   :  |-,        |   |  ' |   |  ' |   |  '  
|   | :.'||   :  | ; | '\  \    `. :   |  ;/|        '   :  | '   :  | '   :  |  
'   :    ;.   |  ' ' ' : `----.   \|   :   .'        ;   |  ; ;   |  ; ;   |  ;  
|   |  ./ '   ;  \; /  | __ \  \  ||   |  |-,        `---'. | `---'. | `---'. |  
;   : ;    \   \  ',  / /  /`--'  /'   :  ;/|         `--..`;  `--..`;  `--..`;  
|   ,/      ;   :    / '--'.     / |   |    \        .--,_    .--,_    .--,_     
'---'        \   \ .'    `--'---'  |   :   .'        |    |`. |    |`. |    |`.  
              `---`                |   | ,'          `-- -`, ;`-- -`, ;`-- -`, ; 
                                   `----'              '---`"   '---`"   '---`"  
                                                                                 


        
        """

        self.draw_banner = """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |  _______     | || |      __      | || | _____  _____ | |
| | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || ||_   _||_   _|| |
| |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || |  | | /\ | |  | |
| |   | |    | | | || |   |  __ /    | || |   / ____ \   | || |  | |/  \| |  | |
| |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  |   /\   |  | |
| | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \__|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 


        """

    def status(self):
        click.echo()
        click.echo("{}: {}".format(self.player.name, "⌺" * len(self.player.cards)))
        click.echo("{}: {}".format(self.computer.name, "⌺" * len(self.computer.cards)))
        click.echo()

    def player_win(self, reason, card_human, card_computer):
        click.echo(reason)
        if len(self.war_cards) > 0:
            click.echo("{} won {} extra cards because of WAR".format(self.player.name, len(self.war_cards)))
            for c in self.war_cards:
                self.player.cards.insert(0, c)
            self.war_cards = list()
        self.player.cards.insert(0, card_human)
        self.player.cards.insert(0, card_computer)
        self.status()

    def player_lose(self, reason, card_human, card_computer):
        click.echo(reason)
        if len(self.war_cards) > 0:
            click.echo("{} won {} extra cards because of WAR".format(self.computer.name, len(self.war_cards)))
            for c in self.war_cards:
                self.computer.cards.insert(0, c)
            self.war_cards = list()
        self.computer.cards.insert(0, card_human)
        self.computer.cards.insert(0, card_computer)
        self.status()

    def play(self):
        t = time.time()
        card_human = self.player.cards.pop()
        card_computer = self.computer.cards.pop()
        click.echo()
        click.echo("------------- GET READY! ----------------")
        time.sleep(0.3)
        click.echo("③")
        time.sleep(0.3)
        click.echo("②")
        time.sleep(0.3)
        click.echo("①")
        click.echo()
        time.sleep(0.3)

        answer = click.prompt("What is {} x {}: ".format(card_human.value, card_computer.value), type=int)

        elapsed_time = round(time.time() - t)
        computer_time = self.computer.answer_time()
        is_correct = (answer == card_computer.value * card_human.value)
        if elapsed_time > computer_time:
            return self.player_lose(
                reason="TOO SLOW! You answered in {} seconds, but computer answered in {} seconds".format(
                    elapsed_time,
                    computer_time
                ),
                card_human=card_human, card_computer=card_computer
            )

        if elapsed_time < computer_time and is_correct:
            return self.player_win(
                reason="CORRECT! You answered {}  in {} seconds".format(answer, elapsed_time),
                card_human=card_human, card_computer=card_computer
            )

        if not is_correct:
            return self.player_lose(
                reason="WRONG! You answered in {} but the correct answer is {}".format(
                    answer,
                    card_computer.value * card_human.value
                ),
                card_human=card_human, card_computer=card_computer
            )
        if is_correct and elapsed_time == computer_time:
            click.echo(self.war_banner)
            if len(self.player.cards) == 0 or len(self.computer.cards) == 0:
                click.echo("DRAW! No one win, because war on the last card")
                self.draw = True
                return
            for a in range(0, 3):
                if len(self.player.cards) == 1 or len(self.computer.cards) == 1:
                    break
                self.war_cards.append(self.player.cards.pop())
                self.war_cards.append(self.computer.cards.pop())


@click.command()
@click.option("--player-name", prompt="What is your name?")
@click.option("--number-of-cards", prompt="How many cards do you want to play with?", type=int)
@click.option("--biggest-card", prompt="What is the biggest card?", type=int)
@click.option("--smallest-card", prompt="What is the smallest card?", type=int)
@click.option("--level", prompt="What difficulty level", type=click.Choice(['easy', 'normal', 'hard', 'nightmare']))
def cli(player_name, number_of_cards, biggest_card, smallest_card, level):
    game = Game(
        player_name=player_name,
        number_of_cards=number_of_cards,
        biggest_card=biggest_card,
        smallest_card=smallest_card,
        level=level
    )

    click.echo("-------------- GET READY {} ----------------".format(game.player.name))

    while len(game.player.cards) > 0 and len(game.computer.cards) > 0 or len(game.war_cards) > 0:
        game.play()

    if game.draw:
        click.echo(game.draw_banner)
    elif len(game.player.cards) > 0:
        click.echo(game.win_banner)
    else:
        click.echo(game.lose_banner)


if __name__ == "__main__":
    cli()
