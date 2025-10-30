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

## Analysis Workflow by using the scripts
###STEP 1. Data Preparation Prepare fasta files containing sequences of orthologous genes. We utilized OrthoFinder ver. 2.5.4 (Emms and Kelly 2015) for this purpose. For STEP 2, sequence IDs in the .faa files should be written as the taxon name followed by a number (e.g., >C_robusta148). Before using OrthoFinder, it's recommended to modify the sequence IDs of your transcriptome data accordingly.
###STEP 2. Clustering Ensure that each fasta file contains the longest gene sequence derived from each sample. Also, each file should contain taxa listed in both list1.txt and list2.txt, with a certain minimum number from each list. This operation was performed using a Python script, Clustering.py. Note that Clustering.py might produce an error if there are unnecessary line breaks in the .faa file. To remove these line breaks, use remove_line_breaks.py.
###STEP 3. Multiple Alignment We created a simple script, RunMafft.sh, to automatically align each gene sequence cluster's fasta file sequentially using Mafft (Katoh and Standley 2013).
###STEP 4. Trimming After processing with Mafft, we created another simple script, RuntrimAL.sh, to automatically trim the fasta files sequentially using trimAl (Capella-Gutierrez et al. 2009).
###STEP 5. Concatenating After trimming, the fasta files were concatenated into a single file by using the Python script Concatenate.py.

---

## References
- Emms & Kelly (2015) *Genome Biology* 16:157. (**OrthoFinder**)  
- Katoh & Standley (2013) *Mol. Biol. Evol.* 30(4):772–780. (**MAFFT**)  
- Capella-Gutierrez et al. (2009) *Bioinformatics* 25:1972–1973. (**trimAl**)  

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
