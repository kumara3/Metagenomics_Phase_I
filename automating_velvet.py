'''
Created on Jun 23, 2014

@author: kumara3
The script runs velvet and meta-velvet for different values of K. The rationale is to mind the optimum values for k(known as 
kmer value).The output so produced should be run through velvet-stats to get the assembly statistics. 
'''
import subprocess
import os
import shutil

def automate_velvet():
    jobs_velveth = []
    jobs_velvetg = []
    fname = '/home/kumara3/workspace/Read_simulator/input_data/Metasim_data_test/taxon_profile-Empirical.994f05d5.fna'
    insert_length = 150
    for i in range(21,23,2):
        directory = ('hash_length'+str(i))
        if not os.path.exists(directory):
            os.mkdir(directory)
        else:
            shutil.rmtree(directory)
            os.makedirs(directory)
        cmd_velveth = "velveth %s %d -fasta -shortPaired %s"%(directory,i,fname)
        cmd_velvetg = "velvetg %s -exp_cov auto -cov_cutoff auto -ins_length %d -read_trkg yes -amos_file yes -unused_reads yes"%(directory,insert_length)
        cmd_metavelvetg = "meta-velvetg %s -ins_length %d"%(directory,insert_length)
        
        print cmd_velveth
        print cmd_velvetg
        print cmd_metavelvetg
        proc_velveth = subprocess.Popen(cmd_velveth,shell=True,stdout=subprocess.PIPE)
        proc_velveth.wait()
        proc_velvetg = subprocess.Popen(cmd_velvetg,shell=True,stdin=proc_velveth.stdout,stdout=subprocess.PIPE)
        proc_velvetg.wait()
        proc_metavelvetg = subprocess.Popen(cmd_metavelvetg,shell=True,stdin=proc_velvetg.stdout,stdout=subprocess.PIPE)
        proc_metavelvetg.wait()

    #    jobs_velveth.append(proc_velveth)
    #    jobs_velvetg.append(proc_velvetg)
    
    #for job in jobs:
    #   job.wait()
       
    
automate_velvet()




        
