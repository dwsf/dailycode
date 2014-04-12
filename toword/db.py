#author:zsc347
#create on Apr 12,2014

import mysql.connector
from mysql.connector import errorcode
import config
import time

def db_test():
    coninfo={
            'user':config.DBUSER,
            'password':config.DBPASSWORD,
            'host':config.DBHOST,
            'database':config.DBDATABASE,
            'raise_on_warnings':True
    }
    cnx=None
    try:
        cnx=mysql.connector.Connect(**coninfo)
        print("connect ok!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
        else:
            print(err)
    else:
        cnx.close()
    return cnx

def db_connect():
    coninfo={
            'user':config.DBUSER,
            'password':config.DBPASSWORD,
            'host':config.DBHOST,
            'database':config.DBDATABASE,
            'raise_on_warnings':True
    }
    return mysql.connector.Connect(**coninfo)
    

def db_insert_words(words):
    '''
    words={'apple':[('n','苹果，苹果树')],
           'brake':[('n','制动器'),('vt','刹车')]}
    '''
    cnx=db_connect()
    cursor=cnx.cursor()
    addWordMeaning=("INSERT INTO words"
              "(spell,type,meaning)"
              "VALUES (%s,%s,%s)")
    for word in words.items():
        for tp,meaning in word[1]:
            wordMeaning=(word[0],tp,meaning)
            try:
                cursor.execute(addWordMeaning, wordMeaning)
            except:
                pass
    cnx.commit()
    cnx.close()

def db_word_query_time(queryWord,belong=0):
    cnx=db_connect()
    cursor=cnx.cursor()
    nowdate=time.strftime("%Y-%m-%d",time.localtime())
    query=("INSERT INTO query"
           "(word,querytime,belong)"
           "VALUES (%s,%s,%s)")
    cursor.execute(query,(queryWord,nowdate,belong))
    cnx.commit()
    cnx.close()
    
def db_words_meaning(words):
    wordsMeaning={}
    cnx=db_connect()
    cursor=cnx.cursor()
    inlist=','.join(["'%s'" %x for x in words])
    query=("SELECT spell,type,meaning FROM words "
           "WHERE spell IN (%s)"%inlist)
    print(query)
#     print(query % inlist)
    cursor.execute(query)
    for spell,wtype,meaning in cursor:
        if spell not in wordsMeaning:
            wordsMeaning[spell]=[]
        wordsMeaning[spell].append((wtype,meaning))
    print(wordsMeaning)
    
        
    
def db_query_by_day(day=None):
    if day is None:
        day=time.strftime("%Y-%m-%d",time.localtime())
        

if __name__ == '__main__':
    words={'apple':[('n','苹果，苹果树')],
           'brake':[('n','制动器'),('vt','刹车')]}
#     db_insert_words(words)    
    db_words_meaning(['apple','brake'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass