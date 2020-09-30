

nucleotides = ['A', 'T', 'C', 'G']
nucleotides_complement = {'T':'A', 'A':'T', 'C':'G', 'G':'C'}

def read_FASTA_file(path):
    '''reads a file and returns a list of lines'''
    with open(path, 'r') as f:
        return [l.strip() for l in f.readlines()]
