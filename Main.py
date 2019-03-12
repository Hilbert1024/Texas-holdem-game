# -*- coding: utf-8 -*-
"""
Created on 2018-4-2

@author: Hilbert

#Texas Poker
"""
import numpy as np
import pandas as pd
from collections import Counter
from itertools import combinations
import sys
import warnings
import Probability


def new_deck():
	suits = ['H']*13+['S']*13+['C']*13+['D']*13
	card_val = list(range(1,14))*4
	deck = pd.DataFrame({'Point':card_val,'Suit':suits})
	return deck


def draw1(deck,person=2):
	return deck.sample(person*2)


def draw2(deck):
	return deck.sample(5)


def update(deck,deletecards):
	deck=deck.drop(deletecards.index)
	return deck


def Points(cards):
	if cards.Point.min()==1:
		cards.Point[cards.Point==1]=14
	if {14,13,12,11,10}==set(cards.Point) and cards.Suit.max()==cards.Suit.min():
		points=1000
	elif cards.Point.max()-cards.Point.min()==4 and len(cards.groupby('Point').count())==5 and cards.Suit.max()==cards.Suit.min():
		points=900+cards.Point.max()
	elif cards.groupby('Point').count().Suit.max()==4:
		points=800+Counter(cards.Point).most_common(1)[0][0]
	elif cards.groupby('Point').count().Suit.max()==3 and cards.groupby('Point').count().Suit.min()==2:
		points=700+Counter(cards.Point).most_common(1)[0][0]
	elif cards.Suit.max()==cards.Suit.min():
		points=600+cards.Point.max()
	elif cards.Point.max()-cards.Point.min()==4 and len(cards.groupby('Point').count())==5:
		points=500+cards.Point.max()
	elif cards.groupby('Point').count().Suit.max()==3 and cards.groupby('Point').count().Suit.min()==1:
		points=400+Counter(cards.Point).most_common(1)[0][0]
	elif cards.groupby('Point').count().Suit.max()==2 and len(cards.groupby('Point').count())==3:
		points=300+max(Counter(cards.Point).most_common(2)[0][0],Counter(cards.Point).most_common(2)[1][0])
	elif cards.groupby('Point').count().Suit.max()==2 and len(cards.groupby('Point').count())==4:
		points=200+Counter(cards.Point).most_common(1)[0][0]
	else:
		points=100+cards.Point.max()
	return points


def state(cards):
	length=len(cards)
	combins = [c for c in  combinations(range(length), 5)]
	list_combins=[]
	for i in combins:
		list_combins.append(list(i))
	card_point=[]
	for l in list_combins:
		card_point.append(Points(cards.iloc[l]))
	card_max=max(card_point)
	return card_max


def computer_bet(cards,per_bet,computer,df1,df2,df3):
	key='n'
	if computer<=per_bet:
		key='ay'
		print('Computer All in!')
	elif len(cards)<5:
		key='y'
	elif len(cards)==5:
		if state(cards)<200:
			num=np.random.binomial(1,1-df1.Lose.iloc[0])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<300:
			num=np.random.binomial(1,1-df1.Lose.iloc[1])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<400:
			num=np.random.binomial(1,1-df1.Lose.iloc[2])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<500:
			num=np.random.binomial(1,1-df1.Lose.iloc[3])
			if num:
				key='y'
			else:
				key='n'
		else:
			key='y'
	elif len(cards)==6:
		if state(cards)<200:
			num=np.random.binomial(1,1-df2.Lose.iloc[0])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<300:
			num=np.random.binomial(1,1-df2.Lose.iloc[1])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<400:
			num=np.random.binomial(1,1-df2.Lose.iloc[2])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<500:
			num=np.random.binomial(1,1-df2.Lose.iloc[3])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<600:
			num=np.random.binomial(1,1-df2.Lose.iloc[4])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<700:
			num=np.random.binomial(1,1-df2.Lose.iloc[5])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<800:
			num=np.random.binomial(1,1-df2.Lose.iloc[6])
			if num:
				key='y'
			else:
				key='n'
		else:
			key='y'
	else:
		if state(cards)<200:
			num=np.random.binomial(1,1-df3.Lose.iloc[0])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<300:
			num=np.random.binomial(1,1-df3.Lose.iloc[1])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<400:
			num=np.random.binomial(1,1-df3.Lose.iloc[2])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<500:
			num=np.random.binomial(1,1-df3.Lose.iloc[3])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<600:
			num=np.random.binomial(1,1-df3.Lose.iloc[4])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<700:
			num=np.random.binomial(1,1-df3.Lose.iloc[5])
			if num:
				key='y'
			else:
				key='n'
		elif state(cards)<800:
			num=np.random.binomial(1,1-df3.Lose.iloc[6])
			if num:
				key='y'
			else:
				key='n'
		else:
			key='y'
	return key


def bet(player):
	print('How much do you want to bet?')
	key=input()
	check=True
	try:
		key=int(key)
	except ValueError:
		check=False
	else:
		pass
	while(check):
		if key<1:
			print('Each bet must not less than 1')
			print('How much do you want to bet?')
			key=input()
			try:
				key=int(key)
			except ValueError:
				check=False
			else:
				pass
		else:
			break
	if not check:
		key='n'
	if check and player<key:
		key='ay'
		print('You All in!')
	return key


def count_coin(coin_pool,win,player,computer):
	if win==1:
		player=player+coin_pool
	elif win==0:
		computer=computer+coin_pool
	else:
		player=player+coin_pool/2
		computer=computer+coin_pool/2
	return player,computer


def results(card1,card2):
	combins = [c for c in  combinations(range(7), 5)]
	list_combins=[]
	for i in combins:
		list_combins.append(list(i))
	card1_point=[]
	card2_point=[]
	for l in list_combins:
		card1_point.append(Points(card1.iloc[l]))
		card2_point.append(Points(card2.iloc[l]))
	card1_max=max(card1_point)
	card2_max=max(card2_point)
	print('=====Player\'s Cards=====')
	print(card1)
	print('Max point:',card1_max)
	print('=====Computer\'s Cards=====')
	print(card2)
	print('Max point:',card2_max)
	if card1_max>card2_max:
		print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
		print('            Player Win!      ')
		print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
		win=1
	elif card1_max<card2_max:
		print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
		print('          Computer Win!      ')
		print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
		win=0
	else:
		print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
		print('               Draw!         ')
		print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
		win=-1
	return win


def main():
	warnings.filterwarnings("ignore")
	print('=====Welcome to Texas poker solo system=====')

	#Initialized
	win=0
	turn=0
	per_bet=1
	coin=0
	path = r'C:\Users\Administrator\Desktop\Python\exercise\one exercise a day\09_Texas_poker\train_final.csv'
	train = pd.read_csv(path)
	df1,df2,df3=Probability.DF_pct(train)


	print('Please input your money:')
	try:
		player_coin=int(input())
	except ValueError:
		print('Game Over!')
		sys.exit()
	else:
		pass
	while (not isinstance(coin,int)) or coin<0:
		print('EORRO!\nPlease input your money:')
		player_coin=int(input())
	computer_coin=player_coin
	print('In this game,press \'y\' means yes,\'n\' means no')
	print('Each bet must be integer and not less than 1')
	while True:
		print('Your money:%d'%player_coin)
		print('Computer\'s money:%d'%computer_coin)
		if player_coin==0:
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('              You Lose!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			sys.exit()
		if computer_coin==0:
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('               You Win!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			sys.exit()
		print('Next turn?\n')
		next_turn=input()
		if next_turn=='y':
			pass
		else:
			print('Your money:%d'%player_coin)
			print('Computer\'s money:%d'%computer_coin)
			if player_coin<computer_coin:
				print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
				print('              You Lose!      ')
				print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			elif player_coin==computer_coin:
				print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
				print('                  Draw!      ')
				print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			else:
				print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
				print('               You Win!      ')
				print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			sys.exit()

		turn+=1
		per_bet+=1
		coin_pool=2*per_bet
		player_coin-=per_bet   #盲注
		computer_coin-=per_bet #盲注
		print('=====Turn %d=====\n'%turn)
		print('Your money:%d'%player_coin)
		print('Computer\'s money:%d'%computer_coin)
		print('Blind of this Turn:%d'%per_bet)


		#NEW DECK
		deck=new_deck()
		draw_player=draw1(deck)
		update(deck,draw_player)
		draw_table=draw2(deck)
		card1=draw_player[:2]
		card2=draw_player[2:]
		Allcard1=card1.append(draw_table)
		Allcard2=card2.append(draw_table)
		print('Your cards:\n',card1)


		#BET ORIGIN,Cards:2
		#PLAYER BET
		key=bet(player_coin)
		#IF ALL IN?
		if key=='ay':
			card1=Allcard1
			card2=Allcard2
			if computer_coin>player_coin:
				coin_pool+=player_coin*2
				computer_coin-=player_coin
				player_coin=0
			else:
				print('Computer All in!')
				coin_pool+=(player_coin+computer_coin)
				player_coin=0
				computer_coin=0
			wins=results(card1,card2)
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('           Player Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=0
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			player_coin-=key


		#Computer BET
		key1=computer_bet(card2,key,computer_coin,df1,df2,df3)
		#IF ALL IN?
		if key1=='ay':
			card1=Allcard1
			card2=Allcard2
			wins=results(card1,card2)
			coin_pool+=computer_coin
			computer_coin=0
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			computer_coin-=key
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Call!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')


		#BET ONE,Cards:5
		#Player BET
		card1=card1.append(draw_table[:3])
		card2=card2.append(draw_table[:3])
		print('Your cards:\n',card1)
		key=bet(player_coin)
		#IF ALL IN?
		if key=='ay':
			card1=Allcard1
			card2=Allcard2
			if computer_coin>player_coin:
				coin_pool+=player_coin*2
				computer_coin-=player_coin
				player_coin=0
			else:
				print('Computer All in!')
				coin_pool+=(player_coin+computer_coin)
				player_coin=0
				computer_coin=0
			wins=results(card1,card2)
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('           Player Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=0
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			player_coin-=key


		#Computer BET
		key1=computer_bet(card2,key,computer_coin,df1,df2,df3)
		#IF ALL IN?
		if key1=='ay':
			card1=Allcard1
			card2=Allcard2
			wins=results(card1,card2)
			coin_pool+=computer_coin
			computer_coin=0
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key1=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=1
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			computer_coin-=key
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Call!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')


		#BET TWO,Cards:6
		#Player BET
		card1=card1.append(draw_table.iloc[3])
		card2=card2.append(draw_table.iloc[3])
		print('Your cards:\n',card1)
		key=bet(player_coin)
		#IF ALL IN?
		if key=='ay':
			card1=Allcard1
			card2=Allcard2
			if computer_coin>player_coin:
				coin_pool+=player_coin*2
				computer_coin-=player_coin
				player_coin=0
			else:
				print('Computer All in!')
				coin_pool+=(player_coin+computer_coin)
				player_coin=0
				computer_coin=0
			wins=results(card1,card2)
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('           Player Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=0
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			player_coin-=key


		#Computer BET
		key1=computer_bet(card2,key,computer_coin,df1,df2,df3)
		#IF ALL IN?
		if key1=='ay':
			card1=Allcard1
			card2=Allcard2
			wins=results(card1,card2)
			coin_pool+=computer_coin
			computer_coin=0
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key1=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=1
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			computer_coin-=key
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Call!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')


		#BET THREE,Cards:7
		#Player BET
		card1=Allcard1
		card2=Allcard2
		print('Your cards:\n',card1)
		key=bet(player_coin)
		if key=='ay':
			if computer_coin>player_coin:
				coin_pool+=player_coin*2
				computer_coin-=player_coin
				player_coin=0
			else:
				print('Computer All in!')
				coin_pool+=(player_coin+computer_coin)
				player_coin=0
				computer_coin=0
			wins=results(card1,card2)
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('           Player Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=0
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			player_coin-=key


		#Computer BET
		print('Waiting.....Computer is thinking.....')
		key1=computer_bet(card2,key,computer_coin,df1,df2,df3)
		#IF ALL IN?
		if key1=='ay':
			card1=Allcard1
			card2=Allcard2
			wins=results(card1,card2)
			coin_pool+=computer_coin
			computer_coin=0
			player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)
			continue
		elif key1=='n':
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Quit!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
			print('=====Player\'s Cards=====')
			print(Allcard1)
			print('Max point:',state(Allcard1))
			print('=====Computer\'s Cards=====')
			print(Allcard2)
			print('Max point:',state(Allcard2))
			win=1
			player_coin,computer_coin=count_coin(coin_pool,win,player_coin,computer_coin)
			continue
		else:
			coin_pool+=key
			computer_coin-=key
			print('┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐')
			print('         Computer Call!      ')
			print('└ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘')
		wins=results(card1,card2)
		player_coin,computer_coin=count_coin(coin_pool,wins,player_coin,computer_coin)

if __name__ == '__main__':
	main()