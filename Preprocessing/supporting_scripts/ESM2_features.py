######################################################################################################################################################
#      This program generates Lx33 feature set from an input fasta and outputs in npy format                                                         #
#      Credit: facebookresearch,                                                                                                                     #
#      colab notebook https://colab.research.google.com/github/facebookresearch/esm/blob/master/examples/contact_prediction.ipynb                    #
######################################################################################################################################################
import esm
import torch
import os
from Bio import SeqIO
import itertools
from typing import List, Tuple
import string
import numpy
torch.set_grad_enabled(False)
import numpy as np
import operator
import numpy as np
import optparse
parser=optparse.OptionParser()
parser.add_option('-i', dest='in_seq',
        default= '',    #default empty!'
        help= 'Input alignment')
parser.add_option('-o', dest='out_npy',
        default= '',    #default empty!'
        help= 'output alignment embed feature')

(options,args) = parser.parse_args()

in_seq = options.in_seq
out_npy = options.out_npy

deletekeys = dict.fromkeys(string.ascii_lowercase)
deletekeys["."] = None
deletekeys["*"] = None
translation = str.maketrans(deletekeys)

def read_sequence(filename: str) -> Tuple[str, str]:
    """ Reads the first (reference) sequence from a fasta or MSA file."""
    record = next(SeqIO.parse(filename, "fasta"))
    print(record)
    return record.description, str(record.seq)

def remove_insertions(sequence: str) -> str:
    """ Removes any insertions into the sequence. Needed to load aligned sequences in an MSA. """
    return sequence.translate(translation)

seq_transformer, seq_alphabet = esm.pretrained.esm2_t33_650M_UR50D()
seq_transformer = seq_transformer.eval()#.cuda()
seq_batch_converter = seq_alphabet.get_batch_converter()
seq_data = [
    read_sequence(in_seq)]
seq_batch_labels, seq_batch_strs, seq_batch_tokens = seq_batch_converter(seq_data)
seq_np = seq_batch_tokens.numpy()
out1 = seq_transformer(seq_batch_tokens)
out2 = out1['logits'].numpy()
np.save(out_npy, out2)
