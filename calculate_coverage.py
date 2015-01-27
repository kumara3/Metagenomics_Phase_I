'''
Created on Aug 1, 2014

@author: kumara3
This script calculates the base coverage and the kmer coverage in velvet
Input parameters : Read length, Number of sequences or reads
Output : Base coverage
'''
import os
from sys import argv
import re

script,pathname,sizepath,readlength,number_reads = argv

filename = os.path.abspath(pathname)
sizename = os.path.abspath(sizepath)

if os.path.exists(filename) and os.path.exists(sizename):
    print "Your filename seems write. We will go ahead and process your data....."
else:
    raise TypeError, "Wrong file"

def calculate_base_coverage(filename,size,readlength):
    coverage_list=[]
    size_dict = {}
    filehandle = open(filename,'r')
    species_reads_dict = {}
   
    for line in filehandle:
        line = line.strip()
        reg_match = re.match(r'^(\d+)\s+Reads\:\s+\`(.*)\'',line)
        if reg_match:
            if reg_match.group(2) not in species_reads_dict:
                species_reads_dict[reg_match.group(2)] = reg_match.group(1)
            else:
                species_reads_dict[reg_match.group(2)].append(reg_match.group(1))
              
    filehandle_second = open(size,'r')
    filehandle_third = open('coverage_information','w')
    for each in filehandle_second:
        reg_sizematch = re.match(r'^(\w+.*)\,(.*)\,(.*)',each)
        size_dict[reg_sizematch.group(1)]=reg_sizematch.group(2) 
    try:
        for key_size in size_dict:
            Total_reads,Total_size,coverage, = 0,0,0,
            for i in species_reads_dict:
                if key_size in i:
                    Total_reads = int(readlength)*int(species_reads_dict[i])
                    Total_size = (float(size_dict[key_size]))
                    coverage = Total_reads*(1e-6)/Total_size
                    
                    coverage_list.append(coverage)
                    filehandle_third.write("The base coverage of %s is %f"%(i,coverage))
                    filehandle_third.write("\n")
                
    except:
        raise TypeError,"Check the Read length. It should be an integer"
        
    return coverage_list, species_reads_dict

def calculate_average(average_list,average_dict):#Calculates average coverage of all the species/genomes
    average = sum(average_list)/len(average_dict)
    print "Average of coverage was found to be %f"%(average)  
      

def calculate_metagenome_coverage(average_dict,size):#Calculate the coverage of metagenome
    size_dict={}
    size_of_metagenome = []
    filehandle_fourth = open(size,'r')
    #filehandle_fourth = open('total_coverage_metagenome','w')
    Total_bases = int(readlength)*int(number_reads)
    for each in filehandle_fourth:
        genome_size,abundance,genome_total_size = 0.0,0.0,0.0
        reg_sizematch = re.match(r'^(\w+.*)\,(.*)\,(.*)',each)
        #print reg_sizematch.group(1),":",reg_sizematch.group(2),":", reg_sizematch.group(3)
        genome_size = reg_sizematch.group(2)
        abundance= reg_sizematch.group(3)
        genome_total_size = float(genome_size)*float(abundance)
        #reg_sizematch.group(1),":",genome_size,":", abundance,":",
        
        size_dict[reg_sizematch.group(1)]=genome_total_size
         
    for k in average_dict:
        for i in size_dict:
            if i in k:
                size_of_metagenome.append(size_dict[i])
    Total_coverage_metagenome = Total_bases/sum(size_of_metagenome)*(1e-6)
    print "The Total metagenome coverage is %f"%(Total_coverage_metagenome)
    
required_list,required_dict=calculate_base_coverage(filename,sizename,readlength)
calculate_average(required_list,required_dict)
calculate_metagenome_coverage(required_dict,sizename)


