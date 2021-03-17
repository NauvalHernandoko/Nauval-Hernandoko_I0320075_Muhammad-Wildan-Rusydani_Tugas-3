#list 10 nama teman
list_teman = ['nando','arfan','irfan','hidan','jefri','narista','issa','harry','ivan','vika']
print("list teman:" ,list_teman)
print("list teman index ke 4,6,7 :",list_teman[4],list_teman[6],list_teman[7])

print('===========================================================================')

list_teman[3] = 'hafiz'
list_teman[5] = 'lazuardi'
list_teman[9] = 'yazid'
print("list teman baru:" ,list_teman)

print('===========================================================================')

list_teman.append('bukhari')
list_teman.append('agna')
print("tambah teman:" ,list_teman)

print('===========================================================================')

for teman in list_teman :
    print(teman)

print('===========================================================================')

print("ada {} teman".format(len(list_teman)))