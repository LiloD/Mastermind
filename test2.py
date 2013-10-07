from mastermind import *
import math
# cb = CodeBreaker()
# print cb.previous_code
# print cb.get_another_code(cb.previous_code)
# print len(cb.get_another_code(cb.previous_code))

cm = CodeMaker((2,7,1,4))
cb = CodeBreaker()

hint = cm.check(cb.previous_code)

print cb.previous_code
print hint
cb.get_hint(hint)
print cb.previous_code
h1 = cm.check(cb.previous_code)
print h1
cb.get_hint(h1)
c2 = cb.previous_code
print c2
h2 = cm.check(c2)
print h2
cb.get_hint(h2)
c3 = cb.previous_code
print c3
h3 = cm.check(c3)
print h3
cb.get_hint(h3)
c4 = cb.previous_code
print c4
h4 = cm.check(c4)
print h4
cb.get_hint(h4)
c5 = cb.previous_code
print c5

# turn = 1

# while hint != (4,0):
# 	print "-----"+str(turn)+"-------"
# 	cb.get_hint(hint)
# 	print cb.previous_code
# 	hint = cm.check(cb.previous_code)
# 	print hint
# 	turn = turn+1
# print "-----"+str(turn)+"-------"

# print math.log(2)
# print math.exp(1.6)
# print math.exp(0.69314718056

# hint2 = cm.check(cb2.previous_code)
# print hint2
# print cb2.previous_code
# print cb2.get_fitness_code(cb2.possible_list)

# dict1 = {(1,0):1,(2,0):2}
# print dict1.keys()
# print dict1.values()
# score = (1,0)
# print dict1[score]

# list1 = (1,2,3,4,5)
# for i in list1:
# 	for j in list1:
# 		print (i,j)
