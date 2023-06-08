x = input("Enter your string to be Ceasoned : ")
shift = int(input("Enter the amount of Ceasoning : ")) % 26
ct = []
for i in x:
	if i.isalnum() == True:
		if (ord(i)+shift) > 122 and i.islower() == True:
			ct.append(chr((((ord(i)+shift))-26)))
		elif (ord(i)+shift) > 90 and i.isupper()==True:
			ct.append(chr((((ord(i)+shift))-26)))
		else:
			ct.append(chr((((ord(i)+shift)))))
	else:
		ct.append(i)
print("".join(ct))