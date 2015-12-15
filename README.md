# cluster-after-cleaning

Scripts used after cleaning the transcriptome from contaminants to find the final number of clusters (based on **Corset** - N. M. Davidson and A. Oshlack. Corset: enabling differential gene expression analysis for de novo assembled transcriptomes. Genome Biology 2014, 15:410 doi:10.1186/s13059-014-0410-6) in each dataset.


# FindCluster.py

Find the cluster of each transcript from a list and write it in the output

Developed (in my case) to find the clusters from the transcripts of my final transcriptome 
(after removing the reads from the contaminants) 

**Usage:**
FindCluster.py -i *list* -c *cluster* -o *output*

**Where:** 
- list = list with all the transcripts (one per line)
- cluster = table result from **Corset** *"...-clusters.txt"*, where there are the information of clusters and transcripts
- output = the name of the output file to save the cluster's name

**Options:**
-h for usage help


# gene_number.py 

Take a list of clusters and count only the main clusters and isoforms independently.

Developed (in my case) to use with a list of clusters that were annotated or identified as
as something, to count the number of identified "genes" and "isoforms".

**Usage:**
gene_number.py -i *list* 

**Where:** 
- list = list with all the clusters (one per line)

**Options:**
-h for usage help

