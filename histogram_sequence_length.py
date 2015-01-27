'''
Created on Jul 21, 2014

@author: kumara3

Plots the contig length distribution
'''
import os
from sys import argv
from Bio import SeqIO
import pylab
script,pathname=argv
filename = os.path.abspath(pathname)

if os.path.exists(filename):
    print "good to go"
else:
    raise TypeError, "Wrong file. PLease check the file type"


def contig_length_dist(file):
    sizes = [len(rec) for rec in SeqIO.parse(filename, "fasta")]
    pylab.hist(sizes, bins=20)
    pylab.title("contig lengthy distribution")
    pylab.xlabel("Sequence length (bp)")
    pylab.ylabel("Count")
    pylab.show()
    
contig_length_dist(filename)

    
    
