import random

names ='''Patrick Ging
Owen Yaggy
Haotian Gan
Wenhao Dong
Ishraq Mahid
Raymond Yeung
Kevin Cao
Ivan Lam
Michelle Lo
Christopher Liu
Michael Borczuk
Naomi Naranjo
Ivan Mijacika
Lucas Lee (Lewis Cass)
Josephine Lee
Rayat Roy
Alif Abdullah
William Chen
Justin Zou
Emma Buller
Andy Lin
Rachel Xiao
Andrew Juang
Eliza Knapp
Yuqing Wu
Renggeng Zheng
Shadman Rakib
AnnabelZhang1
Alejandro Alonso
Deven Maheshwari
DavidASC20
Liesel Wong
Aryaman Goenka
Oscar Wang
Tami Takada
Daniel Sooknanan
Cameron Nelson
Yusuf Elsharawy
Austin Ngan
Ella Krechmer
Tomas Acuna
Tina Nguyen
Thomas Yu
Yaying Liang Li
Sadid Ethun
Jesse Xie
Eric Guo
Jonathan Wu
Shyne Choi
Zhaoyu Lin
Joshua Kloepfer
Shriya Anand
Noakai Aronesty
Yoonah Chang
Roshani Shrestha
Theodore Fahey
Qina Liu
Han Zhang
Lucas Tom-Wong
Julia Nelson
Sophie Liu
Angela Zhang
Gavin McGinley'''

names = names.split('\n')
names.sort()
i = random.randint(0,len(names))
print(names[i])
