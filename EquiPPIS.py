#!/usr/bin/python

#  EquiPPIS: E(3) equivariant graph neural network for PPI site prediction
#
#  Copyright (C) Bhattacharya Laboratory 2022
#
#  EquiPPIS is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  EquiPPIS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with EquiPPIS.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

from egnn_clean import *
import argparse
import os
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from dgl.dataloading import GraphDataLoader

import dgl
import math
import numpy as np
import torch
from Dataloader  import buildGraph  
from torch import nn, optim
from torch.nn import functional as F
from torch.utils.data import DataLoader

def to_np(x):
    return x.cpu().detach().numpy()

def test_epoch(epoch, model, dataloader, PARS):
    model.eval()

    for i, (data_feats) in enumerate(dataloader):
        (tgt_name, nodeFeats, xyz_feats, edges, edge_att) = data_feats
        tgt_name  = tgt_name[0]
        #print(tgt_name)
        print('running ' + tgt_name + ' ...')
        #n_nodes = len(nodeFeats[0])
        #n_e = len(edges[0])
        nodeFeats = nodeFeats.to(PARS.device)
        xyz_feats = xyz_feats.to(PARS.device)
        edges[0] = edges[0].to(PARS.device)
        edges[1] = edges[1].to(PARS.device)
        edge_att = edge_att.to(PARS.device)
        nodeFeats = nodeFeats.squeeze()
        xyz_feats = xyz_feats.squeeze()
        edges[0] = edges[0].squeeze()
        edges[1] = edges[1].squeeze()
        edge_att = edge_att.squeeze()
        edge_att = edge_att.unsqueeze(dim=1)

        #print("####### Target ##########")
        # run model forward and compute loss
        pred, xyz = model(nodeFeats, xyz_feats, edges, edge_att)
        pred = torch.nn.Sigmoid()(pred) 
        pred = pred.detach().numpy()
        #print(pred)
        fo = open(PARS.outdir + '/' + tgt_name + '.out', 'w')
        for pr in pred:
            fo.write(str(pr[0]) + '\n')
        fo.close()
        print('done!')


def print_usage():
    print("\nUsage: EquiPPIS.py [options]\n")

    print("Options:")
    print("  -h, --help            show this help message and exit")
    print("  --model MODEL         String name of model (default 'EGNN')")
    print("  --model_state_dict MODEL_STATE_DICT")
    print("                        Saved model")
    print("  --indir INDIR         Path to input data containing distance maps and input features (default 'Preprocessing/')")
    print("  --outdir OUTDIR       Prediction output directory")
    print("                        Number of data loader workers")
    print("  --num_workers NUM_WORKERS")
    print("                        Number of data loader workers (default=4)")


def main(PARS):
    dataset = buildGraph(path=PARS.indir)
    inference_loader = GraphDataLoader(dataset, batch_size=1, shuffle=False)
    # Get Model
    model = EGNN(in_node_nf=118, hidden_nf=256, out_node_nf=1, in_edge_nf=1, n_layers=10,
             attention=True)
    model.load_state_dict(torch.load(PARS.model_state_dict))
    model.to(PARS.device)

    test_epoch(0, model, inference_loader, PARS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', type=str, default='EGNN',
            help="String name of model (default 'EGNN')")
    parser.add_argument('--model_state_dict', type=str, default=None,
            help="Saved model")
    parser.add_argument('--indir', type=str, default='Preprocessing/',
            help="Path to input data containing distance maps and input features (default 'Preprocessing/')")
    parser.add_argument('--outdir', type=str, default='',
            help="Prediction output directory")
    parser.add_argument('--num_workers', type=int, default=4,
            help="Number of data loader workers (default=4)")
    PARS, _ = parser.parse_known_args()

    #basic input check
    if not PARS.model_state_dict: 
        print('Error! Trained model must be provided. Exiting ...')
        print_usage()
        sys.exit()
    if (PARS.outdir == ''):
        print('Error! Path to the output directory must be provided. Exiting ...')
        print_usage()
        sys.exit()

    #existance check
    if not os.path.exists(PARS.model_state_dict):
        print('Error! No such trained model exists. Exiting ...')   
        print_usage()
        sys.exit()
    if not os.path.exists(PARS.indir):
        print('Error! No such input directory exists. Exiting ...')
        print_usage()
        sys.exit()
    if not os.path.exists(PARS.outdir):
        print('Error! No such output directory exists. Exiting ...')
        print_usage()
        sys.exit()

    #header

    print("\n******************************************************************************")
    print("*                          EquiPPIS                                          *")
    print("*   E(3) equivariant graph neural network for PPI site prediction            *")
    print("*         For comments, please email to dbhattacharya@vt.edu                 *")
    print("******************************************************************************\n")
    
    print('PPI sites prediction probablity threshold is set to 0.18')
    print('Residie-level predictions for each target is being saved at ' + PARS.outdir + '\n') 


    seed = 1992 
    torch.manual_seed(seed)
    np.random.seed(seed)
    PARS.device = torch.device('cpu')
    main(PARS)
