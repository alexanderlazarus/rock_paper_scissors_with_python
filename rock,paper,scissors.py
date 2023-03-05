#!/bin/python3
while True:
 print('Epic entertaining game')
player1 = input('player1 input your move ')
player2 = input('player2 input your move ')
if player1 == ('r') and player2 == ('s'):
 print('player1 wins the game')
elif player1 == ('p') and player2 == ('s'):
  print('player2 has won the game') 
elif player1 == ('r') and player2 == ('p'):
   print('player2 has won the game')  
elif player1 == ('s') and player2 == ('p'):
    print('player1 has won the game')
elif player1 == ('p') and player2 == ('r'):
     print('player1 has won the game')
else:
continue
 print('i dont understand this class')