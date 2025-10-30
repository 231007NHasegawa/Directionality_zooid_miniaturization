# Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians

## Overview
Colonial animals, such as ascidians, bryozoans, and corals, consist of modules known as zooids. While zooid miniaturization in colonial animals has been reported since the 1970s, the evolutionary mechanisms and patterns underlying this trend have remained unexplored.  
Our phylogenomic analysis and ancestral-state reconstruction revealed directional reduction in zooid size associated with the evolution of coloniality in Styelidae ascidians.  
This repository contains all datasets, scripts, and supplementary materials supporting the analyses reported in:

> Hasegawa N., Matsubara S., Shiraishi A., Satake H., Kajihara H. (2025).  
> *Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians.*  
> **Molecular Biology and Evolution** (in review).

---

## Repository Contents
- `alignment.fa`: Final concatenated alignment used for phylogenomic inference  
- `partition.txt`: Partition scheme used for both ML and BI analyses  
- `ML_tree.newick`: Maximum-likelihood tree inferred using IQ-TREE  
- `BI_tree.newick`: Bayesian tree inferred using ExaBayes  
- `scripts/`: Python and Bash scripts used for phylogenomic and trait analyses  
- `Supplementary_Figures/` and `Supplementary_Tables/`: Supplementary materials accompanying the paper  
- `command_log.txt`: Representative command lines for PartitionFinder2, ExaBayes, and BayesTraits analyses  

---

## Analysis Workflow
This repository complements the *Materials and Methods* section of Hasegawa et al. (2025).  
All scripts are reusable for other phylogenomic analyses.

### STEP 1. Data Preparation
Prepare FASTA files containing orthologous gene sequences using **OrthoFinder** (Emms & Kelly, 2015).  
Sequence IDs should follow the format `>TaxonName###`.

### STEP 2. Clustering
Extract the longest sequence per gene per taxon using `Clustering.py`.  
Use `remove_line_breaks.py` to clean malformed FASTA files if necessary.

### STEP 3. Multiple Alignment
Align each gene cluster using **MAFFT** (Katoh & Standley, 2013) via `RunMafft.sh`.

### STEP 4. Trimming
Trim aligned FASTA files using **trimAl** (Capella-Gutierrez et al., 2009) with `RunTrimAl.sh`.

### STEP 5. Concatenation
Concatenate trimmed alignments into a single supermatrix using `Concatenate.py`.

---

## References
- Emms & Kelly (2015) *Genome Biology* 16:157. (**OrthoFinder**)  
- Katoh & Standley (2013) *Mol. Biol. Evol.* 30(4):772–780. (**MAFFT**)  
- Capella-Gutierrez et al. (2009) *Bioinformatics* 25:1972–1973. (**trimAl**)

---

## Acknowledgments
We gratefully acknowledge all contributors for sample collection, laboratory assistance, script development, and crowdfunding support.  
A detailed list of acknowledgments is available in the published article.

---

## Citation
If you use any part of this repository, please cite:  
> Hasegawa N. et al. (2025). *Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians.*  
> **Molecular Biology and Evolution** (in review).

---

## License
This repository is released under the CC-BY 4.0 license, allowing reuse with attribution.

