import os


############Usage############
# Place fasta files (.fa), list1.txt, and list2.txt in a same directory as Clustering.py
# Specie names in the list must fit a taxon name in the fasta files.
# Excepting numbers, taxon name (e.g. A_humilis) must be written in list1.txt or list2.txt because A_humilis1, A_humilis2, A_humilis3, ... was written in fasta files.
# Upon execution, fasta files in the directory will be deleted.
# Please save your files in another directory if you use the files for other analyses.
# If you use this scripts in your project, we would appreciate it if you could cite Hasegawa et al. (YEARS).
###############################

# Extract gene name without numbers.
def GetGeneNameWithOutNumber(name):
    newstring = ''.join([i for i in name if not i.isdigit()])
    return newstring


# Get the longest from a string list.
def GetMaxStringFromList(strList):
    maxSize = 0
    maxGeneStr =""
    for str in strList:
        if maxSize < len(str):
            maxSize = len(str)
            maxGeneStr=str
    return maxGeneStr



# Remove duplicates of species from each fasta file.
# Extract gene name and the longest gene data from the fasta files.
def StoreMaxGeneData(filePath):
    f = open(filePath, 'r')
    dataList = f.readlines()

    index=0
    resultGeneList = []
    tmpGeneList=[]


    beforeGeneName = GetGeneNameWithOutNumber(dataList[0])
    geneName=beforeGeneName
    
    for data in dataList:       
        if index % 2 == 0:
        
            geneName = GetGeneNameWithOutNumber(data)

        
            if beforeGeneName != geneName:
               maxGeneStr = GetMaxStringFromList(tmpGeneList)
               resultGeneList.append([beforeGeneName,maxGeneStr])
               tmpGeneList=[]

            beforeGeneName = geneName
        else:
            tmpGeneList.append(data)

        index = index+1      


        if index == len(dataList):
               maxGeneStr = GetMaxStringFromList(tmpGeneList)
               resultGeneList.append([geneName,maxGeneStr])


    f.close()
    return resultGeneList



# Check how many items from TargetList are contained in geneList
def CheckCountContainList(geneList,targetList):
    sum=0
    for gene in geneList:
        tmpGeneName = gene[0]
        geneName=tmpGeneName[1:]
        if geneName in targetList:
            sum=sum+1
    return sum


# Create output directory
output_dir = "out"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


###################MAIN########################
# List 1
list1File = open("list1.txt", 'r')
list1 = list1File.readlines()
list1File.close()

# List 2
list2File = open("list2.txt", 'r')
list2 = list2File.readlines()
list2File.close()

fileList = os.listdir('./')

# Minimum number of species from list1.txt
targetNum_list1=30  # Please change the number "30" for fitting your analysis.
# Minimum number of species from list2.txt
targetNum_list2=7   # Please change the number "30" for fitting your analysis.

# Debug log flag
isDebugLog=True
# File deletion flag
isDeleteFile=True

# Flag to create processed data
isCreateProcessFile=True

# Extract only .fa files
for file in fileList:
    if(".fa" in file):
        # Eliminate duplicates by species from within each fasta file.
        geneList = StoreMaxGeneData(file)
        # for debug
        if isDebugLog:
            for gene in geneList:            
                print("NAME = "+gene[0])
                print("GENE = "+gene[1])


        # If a fasta file does not contain more than N (the number you specified) species in list1, the fasta is deleted.
        containList1Num = CheckCountContainList(geneList,list1)
        # containList1Num= the number contained the species in a file
        print("List1Check = "+ str(containList1Num))

        #no more than N
        if(containList1Num <= targetNum_list1):
            if isDeleteFile:
                print("List1Check: "+str(targetNum_list1)+"no_more_than " + file)
                #remove the file
                os.remove(file)
            continue

# If a fasta file does not contain more than M (the number you specified) species in list1, the fasta is deleted.
        containList1Num = CheckCountContainList(geneList,list2)
        #containList2Num= the number contained the species in a file
        print("List2Check = "+ str(containList1Num))

        #no more than M
        if(containList1Num <= targetNum_list2):
            if isDeleteFile:
                print("List1Check: "+str(targetNum_list2)+"no_more_than " + file)
                #remove the file
                os.remove(file)
            continue

        if isCreateProcessFile:
            newPath = os.path.join(output_dir, "processed_" + file)
            # Create a new file.
            with open(newPath, mode='w') as f:
                for gene in geneList:            
                    f.write(gene[0])
                    f.write(gene[1])
