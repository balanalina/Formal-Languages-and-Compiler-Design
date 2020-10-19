from symbol_table_impl.hash_table import HashTable

""" mini_language
start
	int count= 0
	strings student1 = 17, student2 = 19, student3 = 18, student4 = 17
	count+=1 if student1 >= 18
	count+=1 if student2 >= 18
	count+=1 if student3 >= 18
	count+=1 if student4 >= 18
	write count + " students can vote!"
end
"""

symbol_table = HashTable(15)   # default capacity for hash table is 50
print('count inserted on position: ' + str(symbol_table.insert('count')))
symbol_table.insert('student1')
print('student2 inserted on position: ' + str(symbol_table.insert('student2')))
symbol_table.insert('student3')
symbol_table.insert('student4')
symbol_table.insert(18)
print('student4 can be found at position ' + str(symbol_table.look_up('student4')))
symbol_table.pretty_pint()


