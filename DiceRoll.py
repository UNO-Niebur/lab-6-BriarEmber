#DiceRoll.py
#Name:Devyn Conaway
#Date:2/28/2026
#Assignment:Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls[dice1 + dice2 - 1] = rolls[dice1 + dice2 - 1] + 1
  #find the sum total of the two dice
  total_rolls = sum(rolls)

  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    percentage = round(count / total_rolls * 100, 2)
    print(f"{dice} : {count} {percentage}%")
    dice = dice + 1



if __name__ == '__main__':
  main()
