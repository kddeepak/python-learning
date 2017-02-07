
string ="cup of tea"
string_rev=string[::-1]

splitted=string.split()
print splitted
reverse=splitted[::-1]
print reverse
for i in range(len(reverse)):
	print reverse[i]

k=" ".join(reverse)
print k		

print string_rev
