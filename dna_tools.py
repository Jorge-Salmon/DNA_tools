
from utils import *
from collections import Counter

def check(seq):
    tmp_seq = seq.upper()
    for nuc in tmp_seq:
        if nuc not in nucleotides:
            return 'Not a valid DNA sequence'
    return tmp_seq


def nucleotide_freq(seq):
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
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)


def translate_DNAseq(seq, start_position=0):
    '''Translates DNA sequence into an aminoacid sequence'''
    return ''.join([DNA_Codons[seq[pos:pos+3]] for pos in range(start_position, len(seq) - 2, 3)])


def translate_RNAseq(seq, start_position=0):
    '''Translates DNA sequence into an aminoacid sequence'''
    return ''.join([RNA_Codons[seq[pos:pos+3]] for pos in range(start_position, len(seq) - 2, 3)])


def aminoacid_codon(seq, aminoacid):
    '''Returns percentage of a given aminoacid produced by codons'''
    temp = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            temp.append(seq[i:i+3])
    freq = dict(Counter(temp))
    total_count = sum(freq.values())
    for i in freq:
        freq[i] = round(freq[i] / total_count, 2)
    return freq
