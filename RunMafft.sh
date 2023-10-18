#!/bin/bash

#########Usage#########
# This script is designed to automate the alignment program, Mafft.
# To run this script, you need to have Mafft in your system's PATH.
# If it's not in the PATH, specify the full path to your Mafft installation in the line that executes Mafft.
# By modifying the Mafft options, you can tailor the analysis to suit your research project.
# If you use this script, please cite below:
# Katoh K, Standley DM (2013) MAFFT multiple sequence alignment software version 7: improvements in performance and usability. Molecular Biology and Evolution 30(4): 772–780.
# Naohiro Hasegawa, Shin Matsubara, Akira Shiraishi, Honoo Satake, Noa Shenkar, Hiroshi Kajihara (YEARS) TENTATIVE TITLE: From Solitary to Colonial Accompanying Miniaturization: Ancestral State Reconstruction based on Phylogenomic Analysis of Styelid Ascidians. JOURNAL. VOLUME(ISSUE): PAGES. URL.
#######################

string="processed_"

# In the current directory, find the files that it contained "Processed" in its file name.
for file in *${string}*; do
    # Extract only file names.
    outputName="${file%.*}_mafft.fa"
    mkdir mafft_out
    echo "${outputName}"
    echo "${file}"
    mafft --amino --inputorder "${file}" > mafft_out/"${outputName}"
    
done
