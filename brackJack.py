############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from replit import clear
from art import logo


def blackjack(play_count):
  def total_sum(player):
      total_score = sum(player)
      return total_score

  def check_ace(player):
      if sum(player) > 21:
          if 11 in player:
              position = player.index(11)
              player[position] = 1

  def is_blackjack(player):
      if sum(player) == 21:
          return True
      else:
          return False

  def is_burst(player):
      if sum(player) > 21:
          return True
      else:
          return False

  def print_scores():
      print(
          f"Computer cards are {computer} . Total is {total_sum(computer)}")
      print(f"Your cards are {user} . Total is {total_sum(user)}")

  def you_win():
      print_scores()
      print("You win")

  def computer_win():
      print_scores()
      print("Computer wins")

  def in_play_proc():
    nonlocal user_in_play_flg
    nonlocal comp_in_play_flg

    print(f"Computer's 1st card is {computer[0]}")
    print(f"Your cards are {user} . Total is {total_sum(user)}")

    #ユーザのターン
    if user_in_play_flg == True:
      if input("Do you draw another card? 'y' or 'n':  ") == "y":
        card = random.choice(cards)
        user.append(card)
        check_ace(user)
        print(f"Your cards are {user} . Total is {total_sum(user)}")
        if is_blackjack(user) or is_burst(user):
            user_in_play_flg = False
            comp_in_play_flg = False
      else: #ユーザがひかなかったとき
        user_in_play_flg = False

    #コンピュータのターン
    if sum(computer) <= 16: #コンピュータがもう1枚ひいたとき
      print("computer draws one more card.")
      card = random.choice(cards)
      computer.append(card)
      check_ace(computer)
      if is_blackjack(computer)or is_burst(computer):
        user_in_play_flg = False
        comp_in_play_flg = False
    else: #コンピュータがひかなかったとき
      print("computer does not draw.")
      comp_in_play_flg = False

  def disp_result():
    print("-----game set.-----game result is...")
    #コンピュータがブラックジャックの場合
    if is_blackjack(computer):
      computer_win()
    #コンピュータがバーストの場合
    elif is_burst(computer):
      you_win()
    #ユーザがブラックジャックの場合
    elif is_blackjack(user):
      you_win()
    #ユーザがバーストの場合
    elif is_burst(user):
      computer_win()
    #上のいづれでもない場合
    else:
      computer_score = sum(computer)
      user_score = sum(user)
      if computer_score > user_score:
          computer_win()
      elif computer_score == user_score:
          print_scores()
          print("It's a draw")
      elif computer_score < user_score:
          you_win()

  clear()
  print(logo)
  user_in_play_flg = True
  comp_in_play_flg = True
  user = []
  computer = []
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  print("play count=" + str(play_count))

  # 初回の手札を決める
  for i in range(0, 2):
      card = random.choice(cards)
      computer.append(card)
      card = random.choice(cards)
      user.append(card)

  # コンピュータが勝っていたら
  if is_blackjack(computer):
      user_in_play_flg = False
      comp_in_play_flg = False

  # ユーザが勝っていたら
  if is_blackjack(user):
      user_in_play_flg = False
      comp_in_play_flg = False

  # 初配で勝敗が決まらなかったとき
  while user_in_play_flg or comp_in_play_flg:
    in_play_proc()

  #勝敗を判定するとき
  disp_result()

  #もう１ゲームやるか
  if input("Do you want to play again? 'y' or 'n': ") == "y":
    return "continue"
  else:
    return "end"

#ゲーム開始
if input("Do you want to play blackjack? 'y' or 'n': ") == "y":
  play_count = 1
  while blackjack(play_count) == "continue":
    play_count += 1
  print("bye bye.")
else:
  print("bye.")



