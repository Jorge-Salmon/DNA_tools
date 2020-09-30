
# Computing GC content

from dna_tools import *
from utils import *

FASTA_file = read_FASTA_file('rosalind_gc.txt')
Fasta_dict = {}
Fasta_label = ''

# converting FASTA into a nuc_dictionary
for line in FASTA_file:
    if '>' in line:
        Fasta_label = line
        Fasta_dict[Fasta_label] = ''
    else:
        Fasta_dict[Fasta_label] += line

final_dict = {key: GC_content(value) for (key, value) in Fasta_dict.items()}

final_key = max(final_dict, key=final_dict.get)

print(f'{final_key[1:]}\n{final_dict[final_key]}')
