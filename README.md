# Directionality_zooid_miniaturization

# Overview
### Colonial animals, such as ascidians, bryozoans, and corals, consist of modules known as zooids. While zooid miniaturization in colonial animals has been reported since 1970s, the evolutionary mechanisms and patterns behind this trend have remained unexplored. Our phylogenomic analysis and ancestral state reconstruction inferred that there has been a directional miniaturization of zooids throughout the evolutionary process of colonial ascidians in the Styelidae family. This repository contains the data and resources that supported our findings, and it serves as our academic project repository for the study of zooid miniaturization accompanying the transition from solitary to colonial life forms in ascidians.

# Citation
## If you use the data or scripts from this repository in your research, please cite our paper:
### Naohiro Hasegawa, Shin Matsubara, Akira Shiraishi, Honoo Satake, Noa Shenkar, Hiroshi Kajihara (YEARS) TENTATIVE TITLE: From Solitary to Colonial Accompanying Miniaturization: Ancestral State Reconstruction based on Phylogenomic Analysis of Styelid Ascidians. JOURNAL. VOLUME(ISSUE): PAGES. URL.
### Your suport in citing our work helps to ensure the continued availability and imporovement of these resources.

# Data Contents
## This repository includes the following data and resources:
### Fasta files (.faa) of transcriptomes after quality check in this project
### A partition file used for both maximum likelihood analysis and Bayesian inference analysis
### Tree files in Newick format
### Scripts used for constructing the phylogenomic trees

# Analysis Workflow
### This section serves as a supplementary explanation for the section "Phylogenomic analysis" of Material and Methods in Hasegawa et al. (YEARS). Please refer to this paper as well. While each step can potentially be connected as a pipeline, scripts used in certain steps are applicable to phylogenetic analyses outside of this project. You can download each script from this repository. If you utilize the scripts in your project, we would appreciate it if you could cite Hasegawa et al. (YEARS).

## STEP 1. Data Preparation
### Prepare fasta files containing sequences of orthologous genes. We utilized OrthoFinder ver. 2.5.4 (Emms and Kelly 2015) for this purpose. For STEP 2, sequence IDs in the .faa files should be written as the taxon name followed by a number (e.g., >C_robusta148). Before using OrthoFinder, it's recommended to modify the sequence IDs of your transcriptome data accordingly.

## STEP 2. Clustering
### Ensure that each fasta file contains the longest gene sequence derived from each sample. Also, each file should contain taxa listed in both list1.txt and list2.txt, with a certain minimum number from each list. This operation was performed using a Python script, Clustering.py. Note that Clustering.py might produce an error if there are unnecessary line breaks in the .faa file. To remove these line breaks, use remove_line_breaks.py.

## STEP 3. Multiple Alignment
### We created a simple script, RunMafft.sh, to automatically align each gene sequence cluster's fasta file sequentially using Mafft (Katoh and Standley 2013).

## STEP 4. Trimming
### After processing with Mafft, we created another simple script, RuntrimAL.sh, to automatically trim the fasta files sequentially using trimAl (Capella-Gutierrez et al. 2009).

## STEP 5. Concatenating
### After trimming, the fasta files were concatenated into a single file by using the Python script Concatenate.py.

# References
### OrthoFinder: Emms, D.M. and Kelly, S. (2015) OrthoFinder: solving fundamental biases in whole genome comparisons dramatically improves orthogroup inference accuracy. Genome Biology. 16:157.
### MAFFT: Katoh K, Standley DM (2013) MAFFT multiple sequence alignment software version 7: improvements in performance and usability. Molecular Biology and Evolution 30(4): 772–780.
### trimAl: Capella-Gutierrez S, Silla-Martinez JM, Gabaldon T (2009) trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses. Bioinformatics. 25:1972–1973.

# Acknowledgments
## We extend our gratitude to following persons:
## For collecting biosamples:
### Cati, Masashi Fukuoka, Bar Gabso, Shoichi Hamano, Natsumi Hookabe, Hiroki Iranami, Naoto Jimi, Yosuke Kamata, Hidenori Katsuragawa, Manami Kimura, Yuki Kita, Hisanori Kohtsuka, Hiroshi Kuriyama, Shlomi Levi, Hiroki Matsushita, Ayumi Mizutani, Lion Novak, Takashi Okada, Misato Sako, Nahum Sela, Maki Shirae-Kurabayashi, Shoki Shiraki, Takeo Sugimoto, Aoi Tsuyuki, Naofumi Ueda, Junko Watanabe, and Hiroshi Yonamine
## For lab works:
### Gil Koplovitz and Gal Vered
## For technical support in script development:
### Kei Kitahata
## For academic support in RNA-seq analysis:
### Analytical Center of Suntory Foundation for Life Sciences Bioorganic Research Institute
## For croudfunding support in the academic croudfunding platform "academist":
### Shunji Furukuma, Naoki Hayashi, Miyuki Honda, Hitoki Horie, Sho Hosotani, Yoshiki Iwai, Nami Kenmotsu, Moe, Takehiro Nakamura, Ryoma Nishikawa, Yuichi Sasaki, Tatsuya Shimoyama, Makoto Taniguchi, Daiki Wakita, Takaaki Yonekura, and many others
## For financial support:
### JST SPRING (Grant Number JPMASP2119)
