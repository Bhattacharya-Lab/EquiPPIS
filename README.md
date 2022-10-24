# EquiPPIS
## Abstract
The knowledge of protein-protein interaction provides a crucial steppingstone to drug design and discovery. To mitigate the cost and time consumed by experimental methods for protein-protein interaction site determination, many computational prediction methods have been developed leveraging the recent progress made in machine learning. However, sequence-based prediction methods suffer from the lack of structural information, while structural-based prediction methods with superior performance become impractical in short of experimentally determined monomeric structures that are taken as input. Here we present EquiPPIS, a deep E(3)-equivariant graph neural network capable of learning a more meaningful representation from structural information, that results in a robust model scalable to utilize predicted structures, bridging the gap between sequence-and structure-based methods. In addition, we propose a feature set introducing several novel features; and with reduced computational overhead by avoiding multiple sequence alignment. In a widely used benchmarking dataset, EquiPPIS outperforms the existing state-of-the-art methods by a large margin.
<p>
    <img src="/IMG/EquiPPIS_concept_diagram.png" width="800" />
</p>

