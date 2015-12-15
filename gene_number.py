#!/usr/local/bin/python


"""
Take a list of clusters and count only the main clusters and isoforms independently.

Developed (in my case) to use with a list of clusters that were annotated or identified as
as something, to count the number of identified "genes" and "isoforms".

Usage = gene_number.py -i <list> 

Where: 
list = list with all the clusters (one per line)

Options: -h for usage help
"""

import sys, getopt


# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:",["list="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage =  gene_number.py -i <list> '
    print 'For help use gene_number.py -h'
    sys.exit(99)
    
for opt, arg in opts:
    if len(arg) < 1 and opt == '-h':
        print '\n', 'Take a list of clusters and count only the main clusters and isoforms independently.', '\n'
        print 'Usage = gene_number.py -i <list>'
        print 'Where: list = list with all the clusters (one per line)'
        sys.exit()
    elif len(arg) > 1:
        if opt in ("-i", "list"):
            list = open(arg)
    elif len(arg) < 1:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


cluster_list = []
cluster_iso = []

# Open the list of cluster and save the main cluster name in a list

for cluster in list:
    cluster_id = cluster.rsplit("\n")
    cluster_id = cluster_id[0]
    prefix = cluster.rsplit(".")
    striped_cluster = prefix[0]
    if cluster_id not in cluster_iso:
	    cluster_iso.append(cluster_id)
    if striped_cluster not in cluster_list:
	    cluster_list.append(striped_cluster)

# Print the size of the list or the number of "genes" based in the main cluster classification   

print "\n", len(cluster_list), " total Clusters 'genes' \n"
print len(cluster_iso), " total Clusters including isoforms \n"
