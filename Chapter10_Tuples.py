# Assignment - Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

dictionary = dict();
FileName = input("Enter file:")

if len(FileName) < 1:
    FileName = "mbox-short.txt"
FileHandle = open(FileName)

for line in FileHandle:
    if line.startswith('From '): # Note that if line.startswith('From'): gives different o/p, remember space after From
        words=line.split()
        time=words[5]; hour=time[0:2];
        dictionary[hour]=dictionary.get(hour,0)+1
    else: continue
#print(dictionary)

#DictionaryItems=dictionary.items(); print(DictionaryItems)
SortedDictionaryItems=sorted(dictionary.items()); #print(SortedDictionaryItems)

for k,v in SortedDictionaryItems:
    print(k,v)






