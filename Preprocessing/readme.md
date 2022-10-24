All input PDB chains, [DSSP](input_details/DSSP_readme.md), FASTA, [PSSM](input_details/PSSM_readme.md), and [ESM2](input_details/ESM2_feature_readme.md) files should be inside `input/` directory

All distance maps should be inside `distmaps/`. An example distance map can be found [here](distmaps/1e96B.dist)

Target list: `input.list`

1. Run `gen_aa_structural_features.py` (feature files will be saved in `tmp/` directory)

`python gen_aa_structural_features.py -t input.list`

2. Run `genpssmto20feat.py` (feature files will be saved in `tmp/` directory)

`python genpssmto20feat.py  -i input -o tmp/ -t input.list`

3. Run `gen_preprocessed_node_features.py` to get combined (1D) 118xL features generated in `processed_features/` directory

`python gen_preprocessed_node_features.py -t input.list`
