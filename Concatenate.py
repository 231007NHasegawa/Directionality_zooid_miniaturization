
import os

###################Usage###################
# The prerequisite for using this script is that there are no duplicate files in the input file.
# Put the fasta files (.fa) you want to concatenate in the current directory.
# The script will not produce an error even if there are line breaks in the text data.
# A concatenated .fa file named "Concatenate.fa" will be created.
# Additionally, a "GeneIndexData.txt" will be generated simultaneously, indicating where in "Concatenate.fa" each gene sequence is located. This text file can be used for partitioning your alignment file.
# If you use this script for your analysis, we would appreciate it if you could cite the following.
# Naohiro Hasegawa, Shin Matsubara, Akira Shiraishi, Honoo Satake, Noa Shenkar, Hiroshi Kajihara (YEARS) TENTATIVE TITLE: From Solitary to Colonial Accompanying Miniaturization: Ancestral State Reconstruction based on Phylogenomic Analysis of Styelid Ascidians. JOURNAL. VOLUME(ISSUE): PAGES. URL.
###########################################

# Extract a gene name and the longest data from fasta files.遺伝子名と一番長い遺伝子データをFAファイルから取り出す
def StoreMaxGeneData(filePath):
    f = open(filePath, 'r')
    # Read line one by one
    dataList = f.readlines()


    # If a line has ">", it means a sequence ID is wwritten in the line.
    # []'A_humili', 'HTNTDAEDEMNRCVISKTKFTDSS…']
    resultGeneList = []

    geneName=""
    sequence=""

    isFirst=True
    index=0
    #Sequence IDs is firstly written.
    for data in dataList:
        if(data[0] ==">"):
            if isFirst==False:
                resultGeneList.append([geneName,sequence])
                sequence=""

            isFirst=False
            geneName=data[1:]
            # Remove line breaks.
            if geneName[-1] == "\n":
                geneName=geneName[:-1]
        else:
            # Remove line breaks.
            if data[-1]=="\n":
                sequence=sequence+data[:-1]
            else:
                sequence=sequence+data

        index=index+1

        # Put sequences data.
        if index == len(dataList):
             resultGeneList.append([geneName,sequence])
    f.close()
    return resultGeneList



#Taking the longest name of sequence ID in the geneDataList.
def GetMaxSequence(geneDataList):
    count=0
    maxGeneName=""
    for geneData in geneDataList:
        sequence=geneData[1]
        if count < len(sequence):
            count=len(sequence)
            maxGeneName=geneData[0]

    #the longest Name
    #print("MaxGeneName= " + maxGeneName)
    return count


#############MAIN######################
fileList = os.listdir('./')


#Writing text data in "geneIndexData.txt" referring gene name and sequence data in all fasta files.
geneDataList=[]

fileListName=[]

for file in fileList:
    if(".fa" in file):
        tmpGeneList = StoreMaxGeneData(file)
        geneDataList.append(tmpGeneList)

        # Extract the second element in the gene names splited like "processed_OG0000000_mafft_trim.fa"
        tmpNameTbl =file.split("_")
        fileListName.append(tmpNameTbl[1])        



#Showing where in "Concatenate.fa" each gene sequence is located.
geneIndexList=[]
index=0

#List all name
geneNameList=[]


print(geneDataList)

# Loop for each gene
for geneData in geneDataList:
    # Taking the maximum number of sequences.
    maxCount= GetMaxSequence(geneData)

    # Store the name and the maximum number in the geneIndexList.
    # Initial
    if(len(geneIndexList)==0):
        geneIndexList.append([fileListName[index], 1,maxCount])
    else:
        beforeMax = geneIndexList[index-1][2]
        geneIndexList.append([fileListName[index], beforeMax+1, beforeMax+maxCount])


    # Loop for a single .fa file
    for gene in geneData:
        # gene name
        geneName=gene[0]
        # checking the name in the list
        if geneName not in geneNameList:
            geneNameList.append(geneName)
    index=index+1



# Result of concatenate
geneConcList=[]
# Put only the names
for name in geneNameList:
    geneConcList.append([name,""])


for geneData in geneDataList:
    # Extracting the muximum number
    maxCount= GetMaxSequence(geneData)

    # Remove genes if they fit
    copyGeneList=[]
    # Initialize every time
    for name in geneNameList:
        copyGeneList.append(name)

    # Loop for a single .fa file
    for gene in geneData:
        #gene name
        geneName=gene[0]
        #sequence
        geneSequence=gene[1]

        # remove from copyGeneList
        if geneName in copyGeneList:
            copyGeneList.remove(geneName)

        # Search in geneConcList
        for i in range(len(geneConcList)):
            # if the gene exist in the list, the number of character in the sequence put in the list.
            if geneConcList[i][0]==geneName:
                isFind=True
                geneLen = len(geneSequence)                
                geneConcList[i][1]=geneConcList[i][1]+geneSequence
                for count in range(maxCount-geneLen):
                    geneConcList[i][1]=geneConcList[i][1]+"-"



    #If there is a gap, "-" is written instead of aa characters.
    for copy in copyGeneList:
        for conc in geneConcList:
            if copy == conc[0]:
                for j in range(maxCount):
                    conc[1]=conc[1]+"-"


# Create Concatenate.fa
newPath='Concatenate.fa'
# Create a new file.
with open(newPath, mode='w') as f:
    for geneData in geneConcList:
        f.write(">" + geneData[0] +"\n")
        f.write(geneData[1])
        f.write('\n')


# Create GeneIndexData.txt
newPath='GeneIndexData.txt'
# Create a new file.
with open(newPath, mode='w') as f:
    for geneIndexData in geneIndexList:
            #OG0000000 = 1-319
            f.write(geneIndexData[0] + " = "+str(geneIndexData[1]) +"-" + str(geneIndexData[2]))
            f.write('\n')
