# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 06:59:11 2017

@author: Alec
"""

import datetime
time = str(datetime.datetime.now())
time = '_' + time[:10].replace('-','_')

send = open('sendfile.txt', 'r')
newsendfiledoc = open('00001.ABI', 'w')
sendfile = send.readlines()
repl = open(str('Replaced_text' + time + '.txt'), 'w')

###Create dict with counter as key and string as values
count = 0
sendfiledict = {}

for i in range(len(sendfile)):
    count+=1
    sendfiledict[count] = sendfile[i]
    
#strip \n
for i  in sendfiledict:
    newstring = sendfiledict[i]
    newstring = newstring[:-1]
    sendfiledict[i] = newstring

###Establish sort criteria
asci = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

###Read value associated with key, modify where no ASCI exist, create new dict
noascisendfiledict = {}
replacedvalues = [] #Traps replaced value and line item position with count

for i in sendfiledict:
    noascistr = ''
    count = 0
    for j in sendfiledict[i]: #for every item in a line, read it, check if it is valid. If valid add to new string, if not, add space.
        ## Possible area for improvement - Create dict for non-asci values
        if j not in asci:
            noascistr += ' '
            count += 1
            replacedvalues.append((j, i, count))
        else:
            noascistr += j
            count += 1
            
    noascisendfiledict[i] = noascistr # creates new dict with valid items    

#print(noascisendfiledict)

for a in noascisendfiledict:
    line = str(noascisendfiledict[a])
    newsendfiledoc.write(line + '\n')

for b in range(len(replacedvalues)):
    replacedval = str(replacedvalues[b])
    repl.write(replacedval + '\n')

send.close()
newsendfiledoc.close()
repl.close()

#def generatesendfile():
#    sendfile = open('sendfile.txt', 'r')
#    newsendfiledoc = open('00001.ABI', 'w')
#    replaceval = open('replaced_values.ABI', 'w')
#    
#    noascisendfiledict, replacedvalues = gen_nonvalidchardict(sendfile)
#    
#    for z in noascisendfiledict:
#        newsendfiledoc.write(z)
#    
#    for a in replacedvalues:
#        replaceval.write(a)
#
#def main():
#    generatesendfile()
#    
#if __name__ == '__main__':
#  main()

#
###send.close()
#newsendfiledoc.close()
#
#print(replacedvalues)
#print(newsendfile)


            
