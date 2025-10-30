# Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians

## Overview
Colonial animals, such as ascidians, bryozoans, and corals, consist of modules known as zooids.  
While zooid miniaturization in colonial animals has been noted since the 1970s, the evolutionary mechanisms and patterns underlying this trend have remained unexplored.  
Our phylogenomic analysis and ancestral-state reconstruction revealed a directional reduction in zooid size associated with the evolution of coloniality in Styelidae ascidians.  
This repository provides all data and resources supporting the analyses reported in:

> Hasegawa N., Matsubara S., Shiraishi A., Satake H., Kajihara H. (2025).  
> *Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians.*  
> **Molecular Biology and Evolution** (in review).

---

## Repository Contents
All files are located in the root directory of this repository.

| File | Description |
|------|--------------|
| `alignment.fa` | Concatenated alignment used for phylogenomic inference |
| `partition.txt` | Partition scheme used for both ML and BI analyses |
| `ML_tree.newick` | Maximum-likelihood phylogenetic tree (IQ-TREE) |
| `BI_tree.newick` | Bayesian phylogenetic tree (ExaBayes) |
| `*.py`, `*.sh` | Python and Bash scripts used for phylogenomic analyses |
| `Supplementary_Figures.pdf` | Supplementary figures accompanying the paper |
| `Supplementary_Tables.xlsx` | Supplementary tables accompanying the paper |

---

## Analysis Workflow Using the Scripts

The following steps describe how each script in this repository can be used to reproduce the phylogenomic analysis conducted in Hasegawa et al. (2025).  
All scripts can be executed in a Linux (WSL) environment and are compatible with standard bioinformatics toolkits.

---

### STEP 1. Data Preparation
Prepare FASTA files containing orthologous gene sequences.  
We utilized **OrthoFinder** ver. 2.5.4 (Emms & Kelly, 2015) for this purpose.  
For the next step, sequence IDs in the `.faa` files should be formatted as the taxon name followed by a unique number (e.g., >C_robusta148). Before running OrthoFinder, it is recommended to standardize the sequence IDs of your transcriptome data accordingly.

---

### STEP 2. Clustering
Ensure that each FASTA file contains the longest gene sequence derived from each sample.  
Each file should also include taxa listed in both `list1.txt` and `list2.txt`, with a minimum number of taxa from each list.  
This step was performed using the Python script **`Clustering.py`**.

> Note:
> `Clustering.py` may return an error if the input FASTA file contains unnecessary line breaks.  
> To remove such line breaks, use the auxiliary script **`remove_line_breaks.py`** prior to clustering.

---

### STEP 3. Multiple Alignment
Run the shell script **`RunMafft.sh`** to automatically align each clustered FASTA file sequentially using **MAFFT** (Katoh & Standley, 2013).  
The script is designed to process all files within a specified directory and output aligned sequences with the suffix `_aligned.faa`.

---

### STEP 4. Trimming
After alignment, execute **`RuntrimAL.sh`** to trim the aligned FASTA files automatically using **trimAl** (Capella-Gutierrez et al., 2009).  
The script removes poorly aligned regions and generates output files with the suffix `_trimmed.faa`.

---

### STEP 5. Concatenation
Once all trimmed alignments are complete, concatenate them into a single supermatrix using the Python script **`Concatenate.py`**.  
This script merges all `.faa` files in the directory into a single alignment file (`alignment.fa`), suitable for downstream phylogenetic analyses.

---

### References for Software
- Emms & Kelly (2015) *Genome Biology* 16:157 — OrthoFinder  
- Katoh & Standley (2013) *Mol. Biol. Evol.* 30(4):772–780 — MAFFT  
- Capella-Gutierrez et al. (2009) *Bioinformatics* 25:1972–1973 — trimAl

---

## Citation
If you use any data or scripts from this repository, please cite:  
> Hasegawa N. et al. (2025). *Spatial competition drives directional zooid miniaturization in colonial stolidobranch ascidians.*  
> **Molecular Biology and Evolution** (in review).

---

## Data Availability
All data supporting this study—including the alignment file, ML and BI tree files, partition file, analysis scripts, and supplementary materials—are available at  
👉 [https://github.com/231007NHasegawa/Directionality_zooid_miniaturization](https://github.com/231007NHasegawa/Directionality_zooid_miniaturization)

---

## License
This repository is distributed under the **CC-BY 4.0** license, allowing reuse with proper attribution.
