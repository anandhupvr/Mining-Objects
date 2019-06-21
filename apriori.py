from itertools import chain, combinations

# pixel = {
# 			1:[[1,3],[1,4],[2,2],[2,3],[2,4],[3,2],[3,3]],
# 			2:[[1,3],[1,4],[2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[4,4]],
# 			3:[[1,3],[1,4],[1,5],[2,3],[2,4],[3,4]],
# 			4:[[1,3],[1,4],[2,3],[2,4],[3,3],[3,4],[5,3],[5,1]],
# 			5:[[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,2]],
# 		}
# # pixel = {
# # 			1:[[1,3],[1,4],[2, 2],[3, 4]],
# # 			2:[[1,3],[1,4],[2,2],[2,3]],
# # 			3:[[1,3],[2, 2],[2,4],[2,3],[3,4]]
# # 		}

def subset(itemset, num):
	return [i for i in combinations(itemset, num)]

def count_subset(itemset):
	lk = {}
	for item in itemset:
		for j in pixel:
			it = [str(i) for i in pixel[j]]
			k = 0
			s = item
			for i in item:
				if i in it:
					k += 1
			if k == len(item):
				if len(item) > 2:
					item = str(s)
					if item in lk:
						lk[item] += 1
					else:
						lk[item] = 1
					item = s
				else:
					if item in lk:
						lk[item] += 1
					else:
						lk[item] = 1			
	return lk


def ifinitem(test, item):
	k = 0
	l = len(item)
	for t in test:
		for i in range(l):
			if item[i] in t:
				k += 1
		if k == l:
			# print ("%s is repeating"%(item))
			return False

	return True

def ifinset(item, sub, l, test):
	k = 0
	for i in range(l):
		if sub[i] not in item:
			item.append(sub[i])
			return item
		else:
			k += 1
	if k == l:

		return []
	elif k == 0:
		return item




def subs(itemset, num):
	test = []
	count = len(itemset)
	for item in itemset:
		l = len(item)
		for j in range(1, count):
			new = [i for i in item]
			new1 = [i for i in itemset[j]]
			m = ifinset(new, new1, l, test)
			if m not in test:
				# print (m)
				if ifinitem(test, m) is True:
					test.append(m)
				else:
					pass
			else:
				pass
				# print ("repeating %s"%(m))

	return test

def filter_support(ck, MinSupport, count):
	L = []
	k = {}
	for i in ck:
		if (ck[i]/count)*100 >= MinSupport:
			L.append(i)
			k[i] = ck[i]
	return sorted(L), k


def Apriori_prune(Ck,MinSupport):
    L = []
    for i in Ck:
        if Ck[i] >= MinSupport:
            L.append(i)
    return sorted(L)

# file = open('example.txt', 'r')
# for line in file:
# 	for item in line.strip().split(' '):
# 		if item in C1:
# 			C1[item] += 1
# 		else:
# 			C1[item] = 1
# file.close()

def num(l):
	C1={}
	import pdb; pdb.set_trace()
	for i in l:
		for line in pixel:
			it = [str(i) for i in pixel]
			if i in it: 
				if i in C1:
					C1[i] += 1
				else:
					C1[i] = 1

def run(pix, sup):
	global pixel
	pixel = pix
	C1={}
	for line in pixel:
		for i in pixel[line]:
			if str(i) in C1:
				C1[str(i)] += 1
			else:
				C1[str(i)] = 1
	# print (C1)
	lm = 3
	# l1 = Apriori_prune(C1, sup)
	l2,c = filter_support(C1, sup, len(pixel))
	# c = num(l2)
	print (c)
	# L = subset(l1, 2)
	# d = count_subset(L)
	# lk = Apriori_prune(d, sup)
	# print (len(lk))
	# # while (lk != []):
	# L = subs(lk, lm)
	# # lk_set = lk
	# # if lm > 3:
	# # 	break
	# # 	L = [x for x in L if x]
	# d = count_subset(L)
	# lk = Apriori_prune(d,sup)
	# lk = [eval(i) for i in lk]
	# print (len(lk))
	# L = subs(lk, lm)
	# d = count_subset(L)
	# lk = Apriori_prune(d,sup)
	# lk = [eval(i) for i in lk]

	return l2
if __name__ == "__main__":
	lk = main(pixel)
	print (lk)