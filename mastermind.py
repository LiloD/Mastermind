import random
import math

print "Hello Master Mind!!"
print "Code : (n1,n2,n3,n4)"
print "Hint : (A,B)"
hint = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]


class CodePartition(object):
	def __init__(self, Code):
		self.code = Code
		self.sets = {(0,0):0,(0,1):0,(0,2):0,(0,3):0,(0,4):0,(1,0):0,(1,1):0,
		(1,2):0,(1,3):0,(2,0):0,(2,1):0,(2,2):0,(3,0):0,(4,0):0}

	def get(self,hint):
		self.sets[hint] = self.sets[hint]+1

	def fitness(self):
		n_sum = 0
		n_right = 0.0
		
		for v in self.sets.values():
			n_sum = n_sum + v
		
		for n in self.sets.values():
			if n > 0:
				n_right = n_right+float(n)/float(n_sum)*math.log(n)
		
		r = math.log(n_sum) - n_right
		return r

	def fitness2(self):
		n_sum = 0
		n_right = 0.0

		for v in self.sets.values():
			n_sum = n_sum + v

		for n in self.sets.values():
			if n > 0:
				n_right = n_right + float(n)*float(n-1)/2

		r = float(n_sum)*float(n_sum-1)/2 - n_right
		return r



class CodeMaker(object):
	"""docstring for CodeMaker"""
	def __init__(self, code):
		self.secret_code = code

	def check(self,Code):
		a,b = 0,0
		for i in self.secret_code:
			for j in Code:
				if i == j:
					b = b+1
		for i in xrange(0,4):
			if self.secret_code[i] == Code[i]:
				a = a+1
		b = b-a
		return (a,b)

class CodeBreaker(object):
	"""docstring for CodeBreaker"""
	def __init__(self):
		self.possible_list = self.init_possible_list()
		self.previous_code = (0,1,2,3)
		# self.previous_code = random.choice(self.possible_list)
		self.current_turn = 1


	def init_possible_list(self):
		r = []
		n1 = 0
		n2 = 0
		n3 = 0
		n4 = 0
		for i in xrange(0,10):
			n1 = i
			for j in xrange(0,10):
				n2 = j
				if n1 == n2:
					continue
				for m in xrange(0,10):
					n3 = m
					if n3 in (n1,n2):
						continue
					for n in xrange(0,10):
						n4 = n
						if n4 in (n1,n2,n3):
							continue
						r.append((n1,n2,n3,n4))
		return r

	def get_hint_entropy(self,hint):
		p_list = []
		cm = CodeMaker(self.previous_code)	
		for c in self.possible_list:
			h = cm.check(c)
			if h == hint:
				p_list.append(c)
		self.possible_list = p_list
		self.previous_code = self.get_fitness_code(p_list)

	def get_hint_randomize(self,hint):
		p_list = []
		cm = CodeMaker(self.previous_code)	
		for c in self.possible_list:
			h = cm.check(c)
			if h == hint:
				p_list.append(c)
		self.possible_list = p_list
		self.previous_code = random.choice(p_list)

	def get_hint_mix(self,hint):
		p_list = []
		cm = CodeMaker(self.previous_code)	
		for c in self.possible_list:
			h = cm.check(c)
			if h == hint:
				p_list.append(c)
		self.possible_list = p_list
		
		if self.current_turn <= 2:
			self.previous_code = random.choice(p_list)
		else:
			self.previous_code = self.get_fitness_code(p_list)

		self.current_turn = self.current_turn+1

	def get_fitness_code(self,possible_set):
		r_list = []
		for i in possible_set:
			cm = CodeMaker(i)
			cp = CodePartition(i)
			for j in possible_set:
				h = cm.check(j)
				cp.get(h)
			f_score = cp.fitness2()
			r_list.append((i,f_score))

		score = 0.0
		code = None
		for s in r_list:
			if(s[1] >= score):
				score = s[1]
				code = s[0]
		#return code
		return code



class MasterMind(object):
	def __init__(self):
		self.input = None

	def set_code(self,code):
		self.code = code

	def run_entropy(self):
		cm = CodeMaker(self.code)
		cp = CodeBreaker()
		hint = None
		while hint != (4,0) :
			c = cp.previous_code
			print c 
			hint = cm.check(c)
			cp.get_hint_entropy(hint)

	def run_randomize(self):
		cm = CodeMaker(self.code)
		cp = CodeBreaker()
		hint = None
		while hint != (4,0) :
			c = cp.previous_code
			print c 
			hint = cm.check(c)
			cp.get_hint_randomize(hint)
	
	def run_mix(self):
		cm = CodeMaker(self.code)
		cp = CodeBreaker()
		hint = None
		while hint != (4,0) :
			c = cp.previous_code
			print c 
			hint = cm.check(c)
			cp.get_hint_mix(hint)
if __name__ == '__main__':
	# mm = MasterMind()
	# mm.set_code((0,1,2,6))
	# mm.run_entropy()	
	# print "---------------------------"
	# mm.run_randomize()

	code = input("Please input the Code: ")
	mm = MasterMind()
	mm.set_code(code)
	mm.run_entropy()
	print "--------------------------------"
	mm.run_randomize()
	print "--------------------------------"
	mm.run_mix()

