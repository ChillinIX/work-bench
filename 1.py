import numpy
import random

p1="Anthony"
p2="Shanise"
p3="Connor"
p4="Colin"
p5="Harry"
p6="Tim"
p7="Shaun"
p8="Ivan"
p9="Tristan"
p10="Ben"

players = (p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
random.shuffle(players)

split = numpy.array_split(players,2)

print ("Radiant: ",split[0])
print ("Dire: ",split[1])