f = open('names.txt', 'r') 
lines = f.readlines()
farr = []

for i in range(len(lines)): 
	temp = lines[i].split()
	farr.append(temp[-1])

f = open('filepath.txt', 'w')

for fpath in farr:
  f.write("%s\n" % fpath)


