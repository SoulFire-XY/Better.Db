import betterdb

f = open(betterdb.db_txt, 'a')
n = input('Enter text: ')
f.write(n)

print('File overided. Text:', n)

f.close()