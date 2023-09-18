# E(3) equivariant graph neural networks for robust and accurate protein–protein interaction site prediction

by Rahmatullah Roche, Bernard Moussad, Md Hossain Shuvo, Debswapna Bhattacharya

published in [PLOS Computational Biology](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011435)

Codebase for our E(3) equivariant graph neural network approach for PPI site prediction, EquiPPIS.

![Workflow](./EquiPPIS.png)

## Installation

1.) We recommend conda virtual environment to install dependencies for EquiPPIS. The following command will create a virtual environment named 'EquiPPIS'

`conda env create -f EquiPPIS_environment.yml`

2.) Then activate the virtual environment

`conda activate EquiPPIS`

3.) Download the trained model for EquiPPIS [here](Trained_model/EquiPPIS_model/E-l10-256.pt)

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
Here is an example of running EquiPPIS:

1.) Input target list and all input files should be inside input preprocessing directory (default `Preprocessing/`). A detailed preprocessing instructions can be found [here](Preprocessing/)

2.) Make an output directory `mkdir output`

3.) Run `python EquiPPIS.py --model_state_dict Trained_model/EquiPPIS_model/E-l10-256.pt --indir Preprocessing/ --outdir output/`

4.) The residue-level PPI site predictions are generated at `output/`. 
