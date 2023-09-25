questions = [
    "What is the capital of India?",
    "What is the currency of Japan?",
    "Who is the current President of the United States?",
    "What is the highest mountain in the world?",
    "Which of the following is a prime number? a) 4 b) 9 c) 11 d) 15"
]

answers = [
    "New Delhi",
    "Yen",
    "Joe Biden",
    "Mount Everest",
    "c"
]

prizes = [
    1000,
    2000,
    5000,
    10000,
    20000
]

# function to check if the answer is correct
def check_answer(question_number, answer):
    if answer.lower() == answers[question_number].lower():
        return True
    else:
        return False

# function to play the game
def play_game():
    total_prize = 0
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i]}")
        answer = input("Enter your answer: ")
        if check_answer(i, answer):
            total_prize += prizes[i]
            print(f"Correct! You won ${prizes[i]}")
        else:
            print("Incorrect. Better luck next time.")
            break
    return total_prize

# function to ask the player if they want to play again
def play_again():
    play_more = input("Do you want to play again? (y/n) ")
    if play_more.lower() == "y":
        return True
    else:
        return False

# main game loop
while True:
    total_prize = play_game()
    print(f"You won a total of ${total_prize}")
    if not play_again():
        break

print("Thank you for playing!")

# aab nia tagra KBC 2, aaj hi try karien.


questions = [
    "What is the capital of India?\n a) New York b) New Jersy c) New Delhi d) New Hampshire",
    "What is the currency of Japan?\n a) Rupee b) Dollar c) Riyal d) Yen",
    "Who is the current President of the United States?\n a) Joe Biden b) Donald Trump c) Bush d) Imran Khan",
    "What is the highest mountain in the world?\n a) K2 b) Mount Everest c) Mount Fiji d) Nanga Parbat",
    "Which of the following is a prime number?\n a) 4 b) 9 c) 11 d) 15",
  "Which language was used to create FB?\n a) Python b)  French c) JavaScript d) PHP",
   "Direction: Three of the following four number pairs are alike in a certain way and one is different. Find the odd one out?\n a) MNOQ b) QSUW  c) BDFH  d) EGIK ",
    "The ratio of present ages of Aslam and Lolita is 5:6 . If the difference between their ages is 6 years , then what will be Lolita’s age after 5 years?\n a)45  b) 41  c) 35  d) 40"
]

answers = [
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b"
]

prizes = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000
]

def chkans(qno, ans):
  if answers[qno].lower() == ans.lower():
    return True
  else:
    return False

def play():
  prize = 0
  for i in range(len(questions)):
    print(f"\n \nQuestion {i+1}: {questions[i]}")
    ans = input("Select the right option: ")
    if chkans(i, ans):
      prize += prizes[i]
      print(f"\nCorrect answer, You have won {prizes[i]}")
    else:
      print("Sorry! Wrong answer")
      break
  return prize

def playagain():
  again = input("\nDo you want to play again: (y/n): ")
  if again.lower() == "y":
    return True
  else:
    return False

while True:
  prize = play()
  print(f"You won ${prize}")
  if not playagain():
    break

if prize == 0:
  print("\n 0 Rs..o ho ..it is not bad luck.. you are nalaik")
else:
  print(f"\n \n \n Thanks for playing. You won Rs {prize}\n tu ru ru tu ru ru ru")

    
  
    
