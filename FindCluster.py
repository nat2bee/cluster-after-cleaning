#!/usr/local/bin/python


"""
Find the cluster of each transcript from a list and write it in the output

Developed (in my case) to find the clusters from the transcripts of my final transcriptome 
(after removing the reads from the contaminants) 

Usage = FindCluster.py -i <list> -c <cluster> -o <output>

Where: 
list = list with all the transcripts (one per line)
cluster = table result from Corset "...-clusters.txt", where there are the information of clusters and transcripts
output = the name of the output file to save the cluster's name

Options: -h for usage help
"""

import sys, getopt

# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:c:o:",["list=","cluster=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage = FindCluster.py -i <list> -c <cluster> -o <output>'
    print 'For help use FindCluster.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 3 and opt == '-h':
        print '\n', 'Find the cluster of each transcript from a list and write it in the output.', '\n'
        print 'Usage =  FindCluster.py -i <list> -c <cluster> -o <output>'
        print 'Where: list = list with all the transcripts (one per line)'
        print 'cluster = table result from Corset "...-clusters.txt", where there are the information of clusters and transcripts'
        print 'output = the name of the output file to save the clusters name'
        sys.exit()
    elif len(arg) > 3:
        if opt in ("-i", "--list"):
            list = open(arg)
        if opt in ("-c", "--cluster"):
            clusters_table = open(arg)
        if opt in ("-o", "--output"):
            output = open(arg,"w")
    elif len(arg) < 3:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"
        
        
# creating variables        
clusters_dict = dict()


# Read the cluster table and save in a dictionary the in formation

for line in clusters_table:
	data = line.split("\t")
	trans_id = data[0]
	cluster_id = data[1]
	cluster_id = cluster_id.rsplit("\n")
	cluster_id = cluster_id[0]
	# Create a dictionary with all the transcripts/clusters
	clusters_dict[trans_id] = cluster_id
	
# For each transcript in my list print the name of its cluster in the output (one per line)

for transcripts in list:
    id = transcripts.rsplit("\n")
    id = id[0]
    id = id.split(">")
    id = id[1]
    cluster = clusters_dict[id]
    output.write(cluster)
    output.write("\n") 
