import handler
import linecache

handler.main()

db_txt = open('locs.txt', 'r')
txt = db_txt.readline()
db_txt.close()

db_dat = open('locs.txt', 'r')
dat = linecache.getline(r'locs.txt', 2)
db_dat.close()
