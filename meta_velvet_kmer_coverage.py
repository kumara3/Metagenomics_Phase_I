#!/usr/bn/python

from numpy import *
import scipy as sp
import rpy2.robjects.lib.plotrix as plotrix
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
stats = importr('stats')
base = importr('base')
datasets = importr('datasets')

mtcars = datasets.data.fetch('mtcars')['mtcars']
data = plotrix.read.table("/home/kumara3/workspace/Read_simulator/hash_length15/meta-velvetg.Graph2-stats.txt", header=TRUE)
weighted.hist("data$short1_cov", "data$lgth", breaks=seq(0, 200, by=1)) 
