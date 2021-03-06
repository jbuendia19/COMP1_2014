# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

######test change#############

import random
import datetime
date = datetime.datetime.now()

NO_OF_RECENT_SCORES = 11

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.date = ''

Deck = [None]
RecentScores = [None]
Choice = ''
AceHighOrLow = False
SameScore = False

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Option')
  print('6. Save Scores')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def DisplayOptions():
  print('Option Menu')
  print()
  print('1. Set Ace to be High or Low')
  print('2. Card of same score ends game')
  print()

def GetOptionChoice():
  valid = False
  OptionChoice = input('Select an option from the menu (or q to quit): ')
  OptionChoice = OptionChoice.lower()
  print()
  while not valid:
    if OptionChoice == '1' or OptionChoice =='q':
      valid = True
    elif OptionChoice == '2':
      valid = True
    else:
      print('Invalid Choice!')
      print()
      OptionChoice = input('Enter a valid choice: ')
  return OptionChoice


def SetOptions(OptionChoice):
  if OptionChoice == '1':
    SetAceHighOrLow()
  elif OptionChoice == '2':
    SetSameScore()


def SetAceHighOrLow():
  global AceHighOrLow
  valid = False
  AceHighOrLow = input('Do you want the Ace to be (h)igh or (l)ow: ').lower()
  print()
  AceHighOrLow = AceHighOrLow[0]
  while not valid:
    if AceHighOrLow == 'h' or AceHighOrLow == 'l':
      valid = True
    else:
      print('Invalid Choice!')
      print()
      AceHighOrLow = input('Enter a valid choice: ')
      valid = False
      print()
  if AceHighOrLow == 'h':
    AceHighOrLow = True
  elif AceHighOrLow == 'l':
    AceHighOrLow = False

def SetSameScore():
  global SameScore
  valid = False
  SameScore = input('Do you want cards with the same value as previuos card to end (y or n): ').lower()
  while not valid:
    if SameScore == 'y' or SameScore == 'n':
      valid = True
    else:
      print('Invalid Choice!')
      SameScore = input('Enter a valid choice: ')
      valid = False
  if SameScore == 'y':
    SameScore = True
  elif SameScore == 'n':
    SameScore = False

def GetMenuChoice():
  Choice = input()
  if Choice in ['Q','quit','Quit']:
    Choice = 'q'
  return Choice

def LoadDeck(Deck):
  global AceHighOrLow
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if AceHighOrLow == True and Deck[Count].Rank == 1:
      Deck[Count].Rank = 14
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher
    

def GetPlayerName():
  valid = False
  print()
  PlayerName = input('Please enter your name: ')
  print()
  while not valid:
    if PlayerName == '':
      PlayerName = input('Please enter a valid name: ')
      print()
      valid = False
    else:
      valid = True
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  if Choice in ['y','yes','Y','Yes']:
    Choice = 'y'
  elif Choice in ['n','no','N','No']:
    Choice = 'n'
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ''

def DisplayRecentScores(RecentScores):
  BubbleSortScores(RecentScores)
  print()
  print('Recent Scores: ')
  print()
  print('{0:<10} {1:<10} {2:<15}'.format('Name','Score','Date'))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print('{0:<10} {1:<10} {2:<15}'.format(RecentScores[Count].Name,RecentScores[Count].Score, RecentScores[Count].date))
  print()
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  HighScore = input('Do you want to add your score to the high score table? (y or n): ')
  print()
  if HighScore == 'y':
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
         FoundSpace = True
      else:
         Count = Count + 1
    if not FoundSpace:
       for Count in range(1, NO_OF_RECENT_SCORES):
         RecentScores[Count].Name = RecentScores[Count + 1].Name
         RecentScores[Count].Score = RecentScores[Count + 1].Score
       Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].date = ('{0}/{1}/{2}'.format(date.day,date.month,date.year))

def BubbleSortScores(RecentScores):
  scores = len(RecentScores)
  swap_made = True
  while swap_made:
    swap_made = False
    scores = scores -1
    for Count in range(1, scores):
      if RecentScores[Count].Score < RecentScores[Count+1].Score:
        temp = RecentScores[Count+1]
        RecentScores[Count+1] = RecentScores[Count]
        RecentScores[Count] = temp
        swap_made = True
  return RecentScores

def SaveScores(RecentScores):
  with open('save_scores.txt', mode='w', encoding='utf-8')as my_file:
    for count in range(1,len(RecentScores)):
      my_file.write((RecentScores[count].Name) + '\n')
      my_file.write(str(RecentScores[count].Score) + '\n')
      my_file.write(str(RecentScores[count].date) + '\n')
      print()
    print('Saved!!')

def LoadScores():
  loaded = False
  RecentScores = ['']
  with open('save_scores.txt', mode = 'r', encoding = 'utf-8')as my_file:
    while not loaded:
      try:
        for count in range(1, NO_OF_RECENT_SCORES + 1):
          scores = TRecentScore()
          scores.Name = my_file.readline().rstrip('\n')
          scores.Score = my_file.readline().rstrip('\n')
          scores.date = my_file.readline().rstrip('\n')
          RecentScores.append(scores)
          loaded = True
      except IOError:
        print('File Not Found!')
        loaded = False
  print('Recent Scores loaded Successfully!')
  return RecentScores
    
def PlayGame(Deck, RecentScores):
  global SameScore
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    if SameScore == True and NextCard.Rank == LastCard.Rank:
      GameOver = True
##    if SameScore == False and NextCard.Rank == LastCard.Rank:
##      GameOver = False
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True      
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  found = False
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  RecentScores = LoadScores()
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
    elif Choice == '6':
      SaveScores(RecentScores)
          
