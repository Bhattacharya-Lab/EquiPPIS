# E(3) equivariant graph neural networks for robust and accurate protein–protein interaction site prediction

by Rahmatullah Roche, Bernard Moussad, Md Hossain Shuvo, Debswapna Bhattacharya

[bioRxiv][pdf]

Codebase for equivariant graph neural network (EquiPPIS) and experiments in the paper.

![Workflow](./EquiPPIS.tif)

## Installation
We recommend conda virtual environment to install dependencies for EquiPPIS. The following command will create a virtual environment named 'EquiPPIS'

`conda env create -f EquiPPIS_environment.yml`

Then activate the virtual environment

`conda activate EquiPPIS`

Download the trained model for EquiPPIS [here](Trained_model/EquiPPIS_model/E-l10-256.pt)

That's it! EquiPPIS is ready to be used.

## Usage

To see usage instructions, run `python EquiPPIS.py -h`

```
usage: EquiPPIS.py [-h] [--model MODEL] [--model_state_dict MODEL_STATE_DICT] [--indir INDIR] [--outdir OUTDIR] [--num_workers NUM_WORKERS]

options:
  -h, --help            show this help message and exit
  --model MODEL         String name of model (default 'EGNN')
  --model_state_dict MODEL_STATE_DICT
                        Saved model
  --indir INDIR         Path to input data containing distance maps and input features (default 'Preprocessing/')
  --outdir OUTDIR       Prediction output directory
  --num_workers NUM_WORKERS
                        Number of data loader workers (default=4)

```
We give an example of running EquiPPIS on several targets as follows.

- Input target list, distance maps and input files should be inside input preprocessing directory (default `Preprocessing/`). A detailed preprocessing instructions can be found [here](Preprocessing/)
- Make an output directory `mkdir output`
- Run `python EquiPPIS.py --model_state_dict Trained_model/EquiPPIS_model/E-l10-256.pt --indir Preprocessing/ --outdir output/`

The residue-level PPI sites predictions are generated at `output/`. 

<b>Coming Soon:</b> More experiments and/or improved implementation of our method! This repo and our paper are still a work in progress.
