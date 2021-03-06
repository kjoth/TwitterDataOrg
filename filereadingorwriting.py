# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import pymysql
#! python
file_object = open('@Mphasis_followers20170321-201720.json', 'r', encoding='utf-8',errors='surrogateescape')
#print(file_object.read())
#a=file_object.readline()
#print(a)


#connect to db
db  = pymysql.connect(host="127.0.0.1",port=3307,user="local",passwd="local",db="mphasistwitterdata",charset="utf8mb4" )

#https://mathiasbynens.be/notes/mysql-utf8mb4#character-sets #Link for utf8mb4

#setup cursor
cursor = db.cursor()

i=0
j=0
k=0
b=[]
for line in file_object.readlines():
    #print("Line : " + str(i) +" " + line)
    #re.match('Count: ', line, flags=0)
    #print("matched")
    
    if k%13==0:
        b=[]
    
    if line.startswith('Count: ') and line.endswith('\n'):
        a=line.partition('Count: ')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
        
        #print(str(line.split()) + 'YES')
    elif line.startswith('User ID 	: ') and line.endswith('\n'):
        a=line.partition('User ID 	: ')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Name 	: ') and line.endswith('\n'):
        a=line.partition('Name 	: ')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Description 	:') and line.endswith('\n'):
        #print('yes')
        #print(str(re.split('Following User ID 	:', line,maxsplit=2,flags=0)).strip())
        a=line.partition('Description 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
        #print(b)
        #print(str(re.split('Following User ID 	:', line, maxsplit=1, flags=0))
        #print(str(line.split()) + 'YES')
    #else: print('NO')
    elif line.startswith('Created at 	:') and line.endswith('\n'):
        a=line.partition('Created at 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Tweets count 	:') and line.endswith('\n'):
        a=line.partition('Tweets count 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Follower count 	:') and line.endswith('\n'):
        a=line.partition('Follower count 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Following count 	:') and line.endswith('\n'):
        a=line.partition('Following count 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Favourites count 	:') and line.endswith('\n'):
        a=line.partition('Favourites count 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('Location 	:') and line.endswith('\n'):
        a=line.partition('Location 	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('verified USer  	:') and line.endswith('\n'):
        a=line.partition('verified USer  	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    elif line.startswith('screen name  	:') and line.endswith('\n'):
        a=line.partition('screen name  	:')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    #elif line.startswith('time_zone 	: ') and line.endswith('\n'):
    elif line.startswith('time_zone 	: '):
        a=line.partition('time_zone 	: ')
        c=a[2]
        c = c.strip('\n')
        #print(c)
        b.append(c)
    #else: break
    #if i==184:
        #print(b)

    i+=1
    j+=1
    k+=1

    if i%13==0:
        
        try:
            cursor.execute("""INSERT INTO mphasis_followers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11],b[12],b[0]))
            #cursor.execute("""INSERT INTO mphasis_following VALUES (%s,%s,%s,%s,%s,%s,%s)""",b[0],b[1],b[2],b[3],b[4],b[5],b[6])
            db.commit()
            j=0
            k=0
        except (pymysql.Error, pymysql.Warning) as e:
            db.rollback()
            print(e)
            print(b)
            print("Unsucessful")    
            break;
        #finally:
            #print(b)
            
        
            
            
        #db.commit()
     
       
    
    #print(line)
    #print(line.strip())
    #print(str(re.split('Following User ID 	:', line, maxsplit=1, flags=0)))

db.close()





    




