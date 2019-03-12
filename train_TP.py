# -*- coding: utf-8 -*-
"""
Created on 2018-4-2

@author: Hilbert

#德州扑克人机solo程序
"""
import numpy as np
import pandas as pd
from collections import Counter
from itertools import combinations
import sys
import random
import warnings


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
	if card1_max>card2_max:
		win=1
	elif card1_max<card2_max:
		win=0
	else:
		win=-1
	return win

def main():
	warnings.filterwarnings("ignore")
	win=0
	N=2000
	df=pd.DataFrame({'Pick1':np.empty(N),'Pick2':np.empty(N),'Pick3':np.empty(N),'Result':np.empty(N)})
	t=0
	while(t<N):
		deck=new_deck()
		draw_player=draw1(deck)
		update(deck,draw_player)
		draw_table=draw2(deck)
		card1=draw_player[:2]
		card2=draw_player[2:]
		Allcard1=card1.append(draw_table)
		Allcard2=card2.append(draw_table)
		card1=card1.append(draw_table[:3])
		df['Pick1'].iloc[t]=state(card1)
		card1=card1.append(draw_table.iloc[3])
		df['Pick2'].iloc[t]=state(card1)
		df['Pick3'].iloc[t]=state(Allcard1)
		df['Result'].iloc[t]=results(Allcard1,Allcard2)
		t+=1
	df.to_csv(r'C:\Users\Administrator\Desktop\Python\exercise\one exercise a day\09_Texas_poker\train_temp.csv')

if __name__ == '__main__':
	main()