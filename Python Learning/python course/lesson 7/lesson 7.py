#Dictionaries
#
band={
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = dict(vocals='Plant', guitar='Page')

print(band)
print(band2)
print(type(band))
print(len(band))


#access items
print(band['vocals'])
print(band.get('guitar'))

#list all keys
print(band.keys())

#print all values

print(band.values())

#list  of key/value pairs as tuples
print(band.items())

#verify a key exists
print('guitar' in band)
print('triangle' in band)

#change values
band['vocals'] = 'coverdale'

band.update({'bass': 'JPJ'})

print(band)

#remove items

print(band.pop('bass'))
print(band)

band['drums'] = 'Bonham'
print(band)


print(band.popitem()) #tuple
print(band)

#delete and clear
band['drums'] = 'Bonham'
del band['drums']


print(band)

band2.clear()
print(band2)

del band2

