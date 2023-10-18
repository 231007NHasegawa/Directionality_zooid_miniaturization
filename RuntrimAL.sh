#!/bin/bash

#########Usage#########
# This script is designed to automate the alignment program, trimAl (Capella-Gutierrez et al. 2009).
# To run this script, you need to have trimal in your system's PATH.
# If it's not in the PATH, specify the full path to your trimal installation in the line that executes Mafft.
# By modifying the trimal options, you can tailor the analysis to suit your research project.
# If you use this script, please cite below:
# Capella-Gutierrez S, Silla-Martinez JM, Gabaldon T (2009) trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses. Bioinformatics. 25:1972–1973.
# Naohiro Hasegawa, Shin Matsubara, Akira Shiraishi, Honoo Satake, Noa Shenkar, Hiroshi Kajihara (YEARS) TENTATIVE TITLE: From Solitary to Colonial Accompanying Miniaturization: Ancestral State Reconstruction based on Phylogenomic Analysis of Styelid Ascidians. JOURNAL. VOLUME(ISSUE): PAGES. URL.
#######################

string="processed_"

# In the current directory, find the files that it contained "Processed" in its file name.
for file in *${string}*; do
    # Extract only file names.
    outputName="${file%.*}_trim.fa"
    echo "${outputName}"
    echo "${file}"
    trimal -in "${file}" -out "${outputName}" -fasta -strictplus
    mkdir -p trimal_out
    mv "${outputName}" -t trimal_out
    
done