#căn giữa trong python
c = '{:^50}'.format('aaaa')
c1 = '{:*^50}'.format('aaaa')
print(c)
print(c1)
#căn trái trong python
a = '{:<50}'.format('aaaa')
a1 = '{:*<50}'.format('aaaa')
print(a)
print(a1)
#căn phải trong python
b = '{:>50}'.format('aaaa')
b1 = '{:*>50}'.format('aaaa')
print(b)
print(b1)

#Ví dụ cụ thể
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
