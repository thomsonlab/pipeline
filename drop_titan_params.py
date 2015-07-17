#######################################
## drop_params.py allows you to change
## the parameters for the drop seq exp
## eriment pipeline.
#######################################
## Developed by:
## Paul Rivaud
## paulrivaud.info@gmail.com
## Summer 2015
#######################################


#######################################
## 									 ##
## Variables the user might modify:  ##
##									 ##
#######################################

####Path to .fastq files
dir_path_fastqs = '../data/drop_test/fastqs/'
#dir_path_fastqs = '../data/fastqs_titan/fastqs/'
#dir_path_fastqs = '../data/fastq_micro/fastqs/'

####Path to .sam files
dir_path_alignment = '../data/drop_test/alignment/'
#dir_path_alignment = '../data/fastqs_titan/alignment/'
#dir_path_alignment = '../data/fastq_micro/alignment/'

####Path to the reference genome files
#mouse_reference_genome = '../reference_genomes/mm9/Transcriptome/transcriptome'
#human_reference_genome = '../reference_genomes/Homo_sapiens/UCSC/hg19/cds'
reference_genome = '../reference_genomes/Human_Mouse/transcriptome'

#######################################
## 									 ##
## Variables that may not be modifed ##
##(Unless you know what you're doing)##
##									 ##
#######################################

#######################
## Preprocessing var ##
#######################

####TAC length:
tac_length = 0

####umi length:
umi_length = 8

####barcode length
barcode_length = 12

####Tso sequence
tso = 'AAGCAGTGGTATCAACGCAGAGTAC'

####Occurence threshold:
occ_threshold = 10000

#######################
##    Bowtie2 var    ##
#######################
bowtie2_dir=''
#Server processors
processors = 8
#Less sensitive 
bowtie2_options = ['-D', '10', '-R', '1', '-N', '0', '-L', '20','-i', 'S,1,0.50', '-p', str(processors), '--reorder', '--no-hd', '--met', '20']
#very sensitive
#bowtie2_options = ['-D', '20', '-R', '3', '-N', '0', '-L', '20','-i', 'S,1,0.50', '-p', str(processors), '--reorder', '--no-hd', '--met', '20']