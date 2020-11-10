#!/usr/bin/env python

from double_helix import double_helix as dna
from utilities import read_FASTA, read_textfile, write_textfile

test_seq = dna()
test_seq.generate_random(40, 'RNA')

for rf in test_seq.open_reading_frames():
    write_textfile('rfs.txt', rf, 'a')
