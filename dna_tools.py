
from utils import *

def check(seq):
    tmp_seq = seq.upper()
    for nuc in tmp_seq:
        if nuc not in nucleotides:
            return 'Not a valid DNA sequence'
    return tmp_seq

def count_nucleotides(seq):
    nuc_dictionary = {'A':0, 'T':0, 'C':0, 'G':0}
    for nuc in seq:
        if nuc in nuc_dictionary:
            nuc_dictionary[nuc] += 1
    return nuc_dictionary

def transcription(seq):
    return seq.replace('T', 'U')

def rev_comlplement(seq):
    return ''.join([nucleotides_complement[nuc] for nuc in seq][::-1])

def GC_content(seq):
    return (seq.count('C') + seq.count('G')) / len(seq) * 100
