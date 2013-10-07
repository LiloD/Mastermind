from mastermind import *

def master_mind(code):
	cm = CodeMaker(code)
	cb = CodeBreaker()
	hint = cm.check(cb.previous_code)

	#print cb.previous_code
	#print hint
	turn = 1

	while hint != (4,0):
		#print "-----"+str(turn)+"-------"
		cb.get_hint_mix(hint)
		# cb.get_hint(hint)
		#print cb.previous_code
		hint = cm.check(cb.previous_code)
		#print hint
		turn = turn+1
	#print "-----"+str(turn)+"-------"
	return turn

#print master_mind((4,7,9,8))
cb2 = CodeBreaker()
full_number = cb2.possible_list
turns = []
index = 0
for i in full_number:
	#turns.append(master_mind(i))
	k = master_mind(i)
	print str(k)+"    No."+str(index)
	turns.append(k)
	index = index+1
#print turns
turn_sum = 0
for n in turns:
	turn_sum = turn_sum+n
print float(float(turn_sum)/float(len(turns))) 