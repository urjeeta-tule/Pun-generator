import io

def main():
	s = check()
	print s
	
def check():

	print "Enter word"
	word = raw_input()	
	
	min_val_line = []
	i = 0
	count = 0
	flag = 1
	

	with io.open(file = '/home/urjeeta/sample.txt', mode = 'r', encoding = 'latin-1') as f:
		for line in f:
			words = line.split()
			val = []
	
			for j in range(len(words)):
				val[j] = lev_dist(word,words[j])
				if similart(words[j],word):
					flag * = 0
				else:
					flag * = 1
			
			if flag == 0:			
				min_val_line[i] = min(val)
				i+=1
				lines[count] = line
				count+=1

	return minimum(min_val_line)
		
def minimum(l):		

	
	MIN = min(l)

	for i in range(len(l)):
		if l[i] == MIN:
			return lines[i]
		else:
			continue

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

def similart(s,t):

	p1 = get_phonemes(s)
	p2 = get_phonemes(t)
	
	for j in p1:
		if j in p2:
			return true
		else:
			continue
	
	return false

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
		else:
			temp=p[i]
			temp=temp+letter			
			p[i]=temp

		F = flagof(letter)

	return p

def flagof(c):

	if c in 'AEIOU' or c in 'aeiou':
		return 0
	else:
		return 1

def startswithvowels(s):

	for c in s:
		if flagof(c) == 0:
			return true
		else:
			return false

