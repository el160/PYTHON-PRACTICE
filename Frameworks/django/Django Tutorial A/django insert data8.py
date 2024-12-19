#the plaeys table that was created in the previous step(models.py)
# #we use python interpreter (python shell) to add some players to it
# we pyhton interpreter to add some players to it using the following command
# py manage.py shell
# the reult should be like:

# Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>>

# at the bottom aftr the three >>> write the command 
# 'from app(players).models import Player' then [enter ]

# to look at the empty table we use the following command
# 'Player.objects.all()'

               # ADDING RECORDS
# add a record to the table using the following command
# "player = Player(firstname='byu',lastname='byu',age=23) [enter]
# player.save() [enter]""

#  to see the record we just added use the following command
# "player.objects.all().values() [enter]""



                       # ADDDING MULTIPLE RECORDS
# you can use bulk_create
#you can also use loops
# you can add multiple records by making a list of player objects and execute .save () on each entry
#>>> player1 = Player(firstname='byu', lastname='jeen', age=32)
#>>> 
#>>> player3 = Player(firstname='mafudi', lastname='baal', age=67)
#>>> player4 = Player(firstname='josue', lastname='punglu', age=21)
#>>> player5 = Player(firstname='isaac', lastname='iza', age=56)
#>>> players_list = [player1, player2, player3, player4, player5]
#for x in players_list:
   # players.save
# players_data = [
#     {'firstname': 'byu', 'lastname': 'jeen', 'age': 32},
#     {'firstname': 'jepy', 'lastname': 'risto', 'age': 45},
#     {'firstname': 'mafudi', 'lastname': 'baal', 'age': 67},
#     {'firstname': 'josue', 'lastname': 'punglu', 'age': 21},
#     {'firstname': 'isaac', 'lastname': 'iza', 'age': 56},
# ]
#>>> for data in players_data:(loop method)
#...  Player.objects.create(**data) - only applies in data presented as dictionaries that is when we the dictionary upacking operator(**)
# players_data = [
#     {'firstname': 'byu', 'lastname': 'jeen', 'age': 32},
#     {'firstname': 'jepy', 'lastname': 'risto', 'age': 45},
#     {'firstname': 'mafudi', 'lastname': 'baal', 'age': 67},
#     {'firstname': 'josue', 'lastname': 'punglu', 'age': 21},
#     {'firstname': 'isaac', 'lastname': 'iza', 'age': 56},
# ] works best
  #or using bulk_create method
  #Player.objects.bulk_create(players)

# to verify that all infor is saved by using this command
# "for player in Player.objects.all():
    #print(player.firstname, player.lastname, player.age)"


