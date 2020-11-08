
from utils import *
from collections import Counter

def check(seq):
    """Checks if sequence is valid"""
    tmp_seq = seq.upper()
    for nuc in tmp_seq:
        if nuc not in nucleotides:
            return 'Not a valid DNA sequence'
    return tmp_seq


def nucleotide_freq(seq):
    """Count of nucleotides in sequence"""
    nuc_dictionary = {'A':0, 'T':0, 'C':0, 'G':0}
    for nuc in seq:
        if nuc in nuc_dictionary:
            nuc_dictionary[nuc] += 1
    return nuc_dictionary


def transcription(seq):
    """DNA transcription --> RNA"""
    return seq.replace('T', 'U')


def rev_comlplement(seq):
    """Calculates reverse complement"""
    return ''.join([nucleotides_complement[nuc] for nuc in seq][::-1])


def GC_content(seq):
    """Returns GC content percentage"""
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


def open_reading_frames(seq):
    """Generates the six open reading frames of DNA"""
    frames = []
    frames.append(translate_DNAseq(seq, 0))
    frames.append(translate_DNAseq(seq, 1))
    frames.append(translate_DNAseq(seq, 2))
    frames.append(translate_DNAseq(rev_comlplement(seq), 0))
    frames.append(translate_DNAseq(rev_comlplement(seq), 1))
    frames.append(translate_DNAseq(rev_comlplement(seq), 2))
    return frames

def prot_rframe(aminoacid_seq):
    '''Returns possible protein between M and Stop'''
    temp_protein = []
    proteins = []
    for i in aminoacid_seq:
        if i == '_':
            # stop appending aminoacids in temp
            if temp_protein:
                for j in temp_protein:
                    proteins.append(j)
                temp_protein = []
        else:
            if i == 'M':
                # start appending aminoacids in temp
                temp_protein.append('')
            for k in range(len(temp_protein)):
                temp_protein[k] += i
    return proteins


def proteins_orfs(seq, start=0, end=0, ordered=False):
    '''Returns all possible proteins from open reading frames'''
    if end > start:
        reading_frames = open_reading_frames(seq[start:end])
    else:
        reading_frames = open_reading_frames(seq)
    proteins_result = []
    for i in reading_frames:
        proteins = prot_rframe(i)
        for j in proteins:
            proteins_result.append(j)
    if ordered:
        return sorted(proteins_result, key=len, reverse=True)
    else:
        return proteins_result
