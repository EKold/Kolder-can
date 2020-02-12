# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:22:51 2019

@author: ejkol
"""

'''Put your header comments here'''

###############################################################################
# Computer Project #9
# Week 12: Scope
#   prompt user for a number between 1-4
#   if user enter 1,sort through files of passwords and display a matching pair
#   if user enter 2,print list of common words inside each password
#   if user enter 3,ask the user for a password and print the entropy of it
#   if user enter 4, exit the program
###############################################################################

from math import log2
from operator import itemgetter
from hashlib import md5
import string
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def open_file(message):
    '''This function taken in a prompt message (string) and returns a file 
    pointer. You likely have a copy from a previous project, but this one adds 
    a default. It repeatedly prompts for a file until one is successfully 
    opened'''

    file = message
    if file == '':
        file = 'pass.txt'
    Done = False
    # a loop is set until a proper file is entered
    while Done != True:
        try:
            fp = open(file, 'r')
            Done = True
            return fp
        except FileNotFoundError:
            print('File not found.')
            file = input('Input a file name: ')
            # if no file is given, the default is pass.txt
            if file == '':
                file = 'pass.txt'
            
def check_characters(password, characters):
    '''This function accepts the password string and a string with the 
    characters to check against as parameters. It returns True if there is at 
    least one matching character anywhere in the string; False otherwise.'''
    #for every letter in characters, if this letter is in password, return True
    
    for letter in characters:
        if letter in password:
            return True
    # else return false
    return False


def password_entropy_calculator(password):
    '''This function takes a string password as input and returns the entropy 
    (float) of the password string'''
    #set variables to use in the calculations
    n = 0
    l = len(password)
    # if the password is blank, n == 0
    if password == '':
        n += 0
    #this checks for specific coditons to be met, and a specific n value is 
    #given to each condition
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == True:
        n += 94
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == True:
        n += 84
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == True:
        n+= 62
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == True:
        n+= 58
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == False:
        n+= 58
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == False:
        n+= 36
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == True:
        n+= 36
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == True:
        n+= 52
    elif check_characters(password, string.ascii_uppercase) == True \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == False:
        n+= 26
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == True:
        n+= 26
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == False:        
        n+= 42
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == False \
    and check_characters(password, string.punctuation) == True \
    and check_characters(password, string.ascii_lowercase) == False:
        n+= 32
    elif check_characters(password, string.ascii_uppercase) == False \
    and check_characters(password, string.digits) == True \
    and check_characters(password, string.punctuation) == False \
    and check_characters(password, string.ascii_lowercase) == False:
        n+= 10   
    #check if n == 0
    if n == 0:
        return 0
    #calculate the entropy and return the value
    entropy = l*log2(n)
    entropy = round(float(entropy),2)
    return entropy
def build_password_dictionary(fp):
    '''This function takes a file pointer parameter of a password file. It 
    reads the file and returns a dictionary of passwords. This dictionary has 
    a password’s MD5 hash as the key, and a tuple as values. The tuple contains
    the password, its rank, and its entropy. '''
    # create an empty dictionary
    password_dict = {}
    rank = 0
    #iterate through the file and set the hash as the dictionary key and a 
    #tuple of data as the value. the tuple has the passwrord,rank,entropy in it
    for password in fp:
        password = password.strip()
        a = tuple()
        rank+= 1
        entropy = password_entropy_calculator(password)
        md5_hash = md5(password.encode()).hexdigest()
        password_dict[md5_hash] = a + (password,rank,entropy)
    return password_dict
        

def cracking(fp,hash_D):
    '''This function takes a file pointer to the password hash file and a 
    password dictionary as parameters. It then uses the password dictionary to 
    crack the password hashes read from the file.'''
    #keep a count of cracked and uncracked passwords
    cracked = 0
    uncracked = 0
    password_list = []
    # for every line, tuple the data and iterate through it
    for line in fp:
        password_tuple = tuple()
        line = line.split(':')
        # if the hash is in the hash file, up cracked count by 1 and appedn the password tuple
        if line[0] in hash_D:
            cracked += 1
            password_tuple += (line[0],hash_D[line[0]][0],hash_D[line[0]][2])
            password_list.append(password_tuple)
        else:
            uncracked += 1
    password_list= sorted(password_list,key=itemgetter(1))
    return password_list, cracked, uncracked
    
            
        
        
def create_set(fp):  
    '''Read file and return data as a set'''
    #create a set of data of the passwords
    set_ = set()
    for line in fp:
        #strip each line and add it to the set
        line = line.strip()
        set_.add(line)
    return set_
        

def common_patterns(D,common,names,phrases):
    '''This function takes the password dictionary 
    (returned by the build_password_dictionary function) and three sets as 
    input and identifies common English words, first names, and phrases 
    contained within the password. It returns a dictionary with the password as
    key and a list of patterns as the value'''
    #have a dictionary
    common_dict = {}
    #for value in improted dictionary, set the value at index 0 to be the key
    for value in D.values():
        common_dict[value[0].lower()] = set()
    for key, value in common_dict.items():
        for word in common:
            #check to see if the word in common file is in the key
            if word.lower() in key:
                #if it is in, then continue, else add it to the dictionary
                if word.lower() in common_dict.values():
                    continue
                else:
                    value.add(word.lower())
        for word in names:
            #same as word in common except now it is word in name file
            if word.lower() in key:
                if word.lower() in common_dict.values():
                    continue
                else:
                    value.add(word.lower())
        for word in phrases:
            #same as word in common except now it is word in phrases file
            if word.lower() in key:
                if word.lower() in common_dict.values():
                    continue
                else:
                    value.add(word.lower())
    #sort the dictonary on the values and return it
    for key, value in common_dict.items():
        common_dict[key] = list(value)
        common_dict[key] = sorted(value)
    return common_dict

def main():
    '''This function prints provided BANNER and MENU and then asks the user to 
    make a choice between the various available options shown in the menu. If 
    the choice is 1, it calls the cracking() function, if it is 2, it calls the 
    common_patterns() function, if it is 3, it calls 
    calculate_password_entropy() function, and if it is 4, it exits. For 
    choices 1 and 2, build a dictionary using build_password_dictionary(), but 
    first use the open_file() function to open the password file (‘pass.txt’).'''
    
    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''
    print(BANNER)
    choice = int(input(MENU))
    Done = True
    #have a loop set to keep prompting for main until user inputs 4
    while Done:
        if choice < 1 or choice > 4:
            print("Error. Try again.")
            choice = int(input(MENU))
        # if choice is one, go through the cracking steps
        elif choice == 1:
            Done = False
            message = input("Common passwords file [enter for default]: ")
            #open the first file
            fp = open_file(message)
            Done = True
            while Done:
                try:
                    #open the hases file
                    hash_fp = input("Hashes file: ")
                    hash_fp = open(hash_fp, 'r')
                    Done = False
                except FileNotFoundError:
                    hash_fp = input("Hashes file: ")
            #build the dictionaries that are needed
            password_dict = build_password_dictionary(fp)
            data = cracking(hash_fp,password_dict)
            data = list(data)
            #pop the required data
            uncracked = data.pop()
            cracked = data.pop()
            #print all the data out
            print("Cracked Passwords:")
            for list_ in data:
                for second_list in list_:
                    print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'.format\
                     ('crack3d!',second_list[0],second_list[1],second_list[2]))
            print('[ i ] stats: cracked {:,d}; uncracked {:,d}'.format\
                                                          (cracked,uncracked))
            #reprompt main
            choice = int(input(MENU))
        #if choice is 2
        if choice == 2:
            Done = False
            message = input("Common passwords file [enter for default]: ")
            #open the first file
            fp = open_file(message)
            password_dict = build_password_dictionary(fp)
            Done = True
            MDone = True
            NDone = True
            #while these are true, attempt to open the specific files
            while Done:
                try:
                    english_words_fp = input("Common English Words file: ")
                    english_words_fp = open(english_words_fp, 'r')
                    Done = False
                except FileNotFoundError:
                    english_words_fp = input("Common English Words file: ")
            common_set = create_set(english_words_fp)
            while MDone:
                try:
                    First_names_fp = input("First names file: ")
                    First_names_fp = open(First_names_fp, 'r')
                    MDone = False
                except FileNotFoundError:
                    First_names_fp = input("First names file: ")
            name_set = create_set(First_names_fp)
            while NDone:
                try:
                    phrases_fp = input("Phrases file: ")
                    phrases_fp = open(phrases_fp, 'r')
                    NDone = False
                except FileNotFoundError:
                    phrases_fp = input("Phrases file: ")
            #create a set of phrases
            phrase_set = create_set(phrases_fp)
            #create a dictioanary of values
            D_patterns= common_patterns\
                              (password_dict, common_set, name_set, phrase_set)
            #print everything out
            print("{:20s}{:20s}".format("Password","Patterns"))
            for k,v in D_patterns.items():
                print("{:20s} [".format(k),end='')# print password
                print(', '.join(v),end=']\n') # print comma separated list
            #prompt for menu
            choice = int(input(MENU))
        #check if choice is 3
        if choice == 3:
            #get the password
            password = input("Enter the password: ")
            entropy = password_entropy_calculator(password)
            #print everythin gout
            print("The entropy of {} is {}".format(password,entropy))
            #remprompt for menu
            choice = int(input(MENU))
        if choice == 4:
            break
            #end program
        
        
        
if __name__ == '__main__':
    main()