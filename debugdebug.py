import io
import os

s = raw_input()
#t = raw_input()

def flagof(c):

	if c in 'AEIOU' or c in 'aeiou':
		return 0
	else:
		return 1

def startswith(s):

	for c in s:
		if flagof(c) == 0:
			return 0
		else:
			return 1


def get_phonemes(s):
	
	p = []
	i = -1	

	F = startswith(s)


	for letter in s:
		
		if i==-1:
			p.append(letter)
			i=i+1
			continue
			
		if (bool(F)!=bool(flagof(letter))) == 1:
			i=i+1
			p.append(letter)
#			print p				
		else:
			temp=p[i]
			temp=temp+letter			
			p[i]=temp
#			print p				

		F = flagof(letter)

	return p

def similart(s,t):

	p1 = get_phonemes(s)
	p2 = get_phonemes(t)
	
	for j in p1:
		if j in p2 and flagof(j)==0:
			print "Similar phonemes"
			return True
		else:
			continue
	print "Not Similar phonemes"
	return False

def simlar(s,t):
	
	if(lev_dist(s,t)==1):
		similart(s,t)
#		print "Puns detected"
		return True
	else:
#		print "Puns not detected"
		return False

def lev_dist(s, t):

	if s == t:        
		return 0
	if len(s) == 0:
		return len(t)
	if len(t) == 0:
		return len(s)

	v0 = list(range(len(t) + 1))
	v1 = [None for _ in range(len(t) + 1)]

	for i in range(len(s)):
		v1[0] = i + 1
	
		for j in range(len(t)):
			cost = 0 if s[i] == t[j] else 1
			v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
	
		for j in range(len(v0)):
			v0[j] = v1[j]
	
	return v1[len(t)]

def findmeidioms():
	
	with io.open(file = os.path.dirname(os.path.realpath(__file__))+'/sample.txt', mode = 'r', encoding = 'latin-1') as f:
		for line in f:
			words = line.split()
			for w in words:
				if simlar(s,w)==True:
					print line.replace(w,s)
					return
			
	print "No such idiom in list"
	

findmeidioms()

