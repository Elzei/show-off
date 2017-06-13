#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'wro00708'

#1
def ex1(number):
    message = {0:"zero", 1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem",
                9:"dziwięć", 10:"dziesięć", 11:"jedenaście", 12:"dwanaście", 13:"trzynaście", 14:"czternaście",
                15:"piętnaście", 16:"szesnaście", 17:"siedemnaście", 18:"osiemnaście", 19:"dziewiętnaście",
              20:"dwadzieścia", 30:"trzydzieści", 40:"czterdzieści", 50:"piędziesiat", 60:"sześdziesiąt",
              70:"siedemdziesiąt", 80:"osiemdziesiąt",90:"dziewiędziesiąt", 100:"sto"}
    if number < 21:
        return message[number][:]
    else:
        print((number//10)*10)
        print(number%10)
        if number%10:
            slowo1 =  "".join(message[((number//10)*10)])
            slowo2 = "".join(message[(number%10)])
            return slowo1+slowo2 #join nie działa ze względu na kodowanie UTF-8. Join działa na kodowaniu ASCII i mu się merda. Spróbuj!
        else:
            return "".join(message[((number//10)*10)])

testy = [0,3,5,12,25,77,98,100]
for i in testy:
    #slowa = ex1(i)
    #tak można łamać kod, za pomocą "\"
    print("Liczba %d to: %s" % \
          (i, ex1(i)))
#2
def ex2():
    for i in range(33, 127):
        if(not i%20):
            print("")
        print(chr(i), end=" " )

#3
def ex3(newString):
    #W stylu C
    sum = 0
    for i in range(0, len(newString)):
        sum = sum + ord(newString[i])
    print(sum)

#4
def ex4(newString):
    longStars = ("*"*(len(newString)+4))
    shortStars = ("*"+(" "*(len(newString)+2))+"*")
    print(longStars)
    print(shortStars)
    print("* "+newString+" *")
    print(shortStars)
    print(longStars)

#5
def ex5(bottom):
    for i in range(1, bottom+1):
        if(i%2):
            print((" "*((bottom-i)//2)), end="")
            for j in range(0,i):
                print("*", end="")
            print("")
"""
def piramida(size):
    for i in range(1, size +1, 2):
        print(" " * ((size-i)//2)+"*"*i)

if __name__ == '__main__':
    piramida(7)
"""
