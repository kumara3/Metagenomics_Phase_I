'''
Created on Aug 20, 2014

@author: kumara3

Input : meta-velvet.contigs.fa 
OUTPUT : x,y coordinate. x is DNA sequence length and y is the number of reads 
'''

from _bisect import bisect
from sys import argv
import os
import csv

script,pathname = argv
fasta_file = os.path.abspath(pathname)

if os.path.exists(fasta_file):
    print "YOU ARE GOOD TO GO"
else:
    raise TypeError," Wrong file has been used as the input"

file_name = pathname+"coordinates"

def readFA(fa_file):
    readfasta = {}
    with open(fa_file) as fp:
        info = fp.readline().rstrip()
        seq=""
        
        while True:
            line=fp.readline()
            if not line or line[0]==">":
                readfasta[info]=seq
                if not line:
                    break
                info = line.rstrip()
                seq = ""
                
            else:
                seq += line.strip()
    return readfasta

return_readfasta = readFA(fasta_file)

def draw_bar(return_fa):
    siz=0
    dict_bar={}
    sizes = ([len(return_fa[key]) for key in return_fa])
    list_bar = [organize(siz)for siz in sizes]
    mapping_dict = {x:y for x,y in zip(['A','B','C','D','E','F','G','H','I','J','K','L'],['1000','2000','3000','4000','5000','6000','7000','8000','9000','10000','11000','>=11000'])}

    try:
        for each_item in list_bar:
            if each_item not in dict_bar:
                dict_bar[each_item] = 1
            else:
                dict_bar[each_item] += 1
    except:
        print "check the bisect algorithm parameter"
    
    with open(file_name,'wb') as fw:
            writer = csv.writer(fw)
            for key,value in dict_bar.items():
                if key in mapping_dict.keys():

                    writer.writerow([mapping_dict[key],value])
    
def organize(sizs,breakpoints=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000],specs='ABCDEFGHIJKL'):
    i = bisect(breakpoints,sizs)
    return specs[i]

draw_bar(return_readfasta)

