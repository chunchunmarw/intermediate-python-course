import random

def main():
  dice_roll = 2
  dice_sum = 0
  for i in range(0,dice_roll):
    roll = random.randint(1,6)
    dice_sum =+ roll
    
    if roll == 1:
      print(f'You rolled a {roll}! critical fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! cirtical success')
    else:
      print(f'You rolled a {roll}')
  print(f'You rolled total of {dice_sum}')
if __name__== "__main__":
  main()
