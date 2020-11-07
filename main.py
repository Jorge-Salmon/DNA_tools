#!/usr/bin/env python

from dna_tools import *
import random

# Random DNA seq
randDNAseq = ''.join([random.choice(nucleotides) for i in range(50)])

DNA_string = check(randDNAseq)

print(f'\nSequence: {DNA_string}\n')
print(f'(1) Sequence length: {len(DNA_string)}\n')
print(f'(2) Nucleotide frequency : {nucleotide_freq(DNA_string)}\n')
print(f'(3) DNA --> RNA trnascription {transcription(DNA_string)}\n')
print(f"(4) DNA string, its complement and reverse complement:\n5' {DNA_string} 3'")
print(f"   {''.join(['|' for i in range (len(DNA_string))])}")
print(f"3' {rev_comlplement(DNA_string)[::-1]} 5' Complement")
print(f"5' {rev_comlplement(DNA_string)} 3' Reverse complement\n")
print(f'(5) GC content: {GC_content(DNA_string)}%\n')
print(f'(6) GC content in substring k= ')
print(f'(7) Aminoacids sequence from DNA: {translate_DNAseq(DNA_string, 0)}\n')
print(f"(7) Codon frequency (L) {aminoacid_codon(DNA_string, 'L')}\n")
