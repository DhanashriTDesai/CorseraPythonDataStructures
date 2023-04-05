# Assignment 

# 9.4 - Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

dictionary = dict();
FileName = input("Enter file:")

if len(FileName) < 1:
    FileName = "mbox-short.txt"
FileHandle = open(FileName)

for line in FileHandle:
    if line.startswith('From '): # Note that if line.startswith('From'): gives different o/p, remember space after From
        words=line.split()
        email=words[1]
        dictionary[email]=dictionary.get(email,0)+1
    else: continue
# print(dictionary)
        
bigemail = None; bigcount = None;
for email,count in dictionary.items():
    print(bigemail,bigcount)
        
        

    

    
    
    








