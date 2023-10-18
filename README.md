# Directionality_zooid_miniaturization

# Overview
### Colonial animals, such as ascidians, corals, and bryozoans, consist of individual units known as zooids. While the phenomenon of zooid miniaturization in colonial animals has been reported, the evolutionary mechanisms and patterns behind this trend have remained unexplored. An ancestral state reconstruction based on a phylogenomic analysis inferred that there has been a directional miniaturization of zooids throughout the evolutionary process of colonial ascidians in the Styelidae family. This repository contains the data and resources that supported our findings, and it serves as our academic project repository for the study of zooid miniaturization accompanying the transition from solitary to colonial life forms in ascidians.

# Citation
## If you use the data or scripts from this repository in your research, please cite our paper:
### Naohiro Hasegawa, Shin Matsubara, Akira Shiraishi, Honoo Satake, Noa Shenkar, Hiroshi Kajihara (YEARS) TENTATIVE TITLE: From Solitary to Colonial Accompanying Miniaturization: Ancestral State Reconstruction based on Phylogenomic Analysis of Styelid Ascidians. JOURNAL. VOLUME(ISSUE): PAGES. URL.
## Your suport in citing our work helps to ensure the continued availability and imporovement of these resources.

# Data Contents
## This repository includes the following data and resources:
### Fasta files of transcriptomes assembled in this project
### A partition file used for both maximum likelihood analysis and Bayesian inference analysis
### Tree files in Newick format
### Scripts used for constructing the phylogenomic trees

# Analysis Workflow
### This section serves as a supplementary explanation for the section "Phylogenomic analysis" of Material and Methods in Hasegawa et al. (YEARS). Please refer to this paper as well. While each step can potentially be connected as a pipeline, scripts used in certain steps are believed to be applicable to phylogenetic analyses outside of this project. You can download each script from this repository. If you utilize the scripts from this workflow in your project, we would appreciate it if you could cite Hasegawa et al. (YEARS).
## STEP 1. Data Preparation
### Prepare fasta files containing sequences information of orthologous genes. We utilized OrthoFinder for this purpose. For STEP 2, sequence IDs in the .faa files should be written as the taxon name followed by a number (e.g., >C_robusta148). Before using OrthoFinder, it's recommended to modify the sequence IDs of your transcriptome data accordingly.

## STEP 2. Clustering
### Ensure that each .faa file contains the longest gene sequence derived from the same species. Also, each .faa file should contain species listed in both list1.txt and list2.txt, with a certain minimum number from each list. This operation was performed using Clustering.py. Note that Clustering.py might produce an error if there are unnecessary line breaks in the .faa file. To remove these line breaks, use remove_line_breaks.py.

## STEP 3. Multiple Alignment
### We created a simple script, RunMafft.sh, to automatically align each gene sequence cluster's .faa file sequentially using Mafft.

## STEP 4. Trimming
### After processing with Mafft, we created another simple script, RuntrimAL.sh, to automatically trim the .faa files sequentially using trimAL.

## STEP 5. Concatenating
### After trimming, the .faa files were concatenated into a single file. The script used for this purpose is Concatenate.py.

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
