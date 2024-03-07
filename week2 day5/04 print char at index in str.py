str1 = 'karthik'

even_char = [] 
odd_char = [] 

for i in range(len(str1)):
	if i % 2 == 0: 
		even_char.append(str1[i])
	else:
		odd_char.append(str1[i])
		
print(odd_char)
print('Odd characters: {}'.format(odd_char)) 

print('Even characters: {}'.format(even_char))
