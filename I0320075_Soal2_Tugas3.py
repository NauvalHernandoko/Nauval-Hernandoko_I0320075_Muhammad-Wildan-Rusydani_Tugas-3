#Membuat program dictionary
dict = {'Name':'Nauval','Hobi1':'bermain musik','Hobi2':'futsal','Hobi3':'bermain game'
        ,'instagram':'@nauvallh','whatsApp':'085804879xxx','line':'nvlh21'
        ,'lagu1':'lose-Niki','lagu2':'di matamu-Armada','lagu3':'antara pagi dan kau-daun jatuh'
        ,'makanan favorit 1':'ayam bakar','makanan favorit 2':'ayam goreng','makanan favorit 3':'steak'}

print("dict:",dict)

dict['Hobi3'] = 'tidur'
dict['instagram'] = '@nauvalhernandoko'

print("dict baru:",dict)

del dict['makanan favorit 1']
del dict['makanan favorit 2']

print("dict baru lagi:",dict)

dict['Hobi baru'] = 'berserah diri'

print("dict baru banget:",dict)