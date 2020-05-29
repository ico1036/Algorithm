import glob
import subprocess

##################################################################
#  * Purpose: run excute.py code with input files			     #
#  * There are many input files									 #
#  * You wan't to run like this:							     #
#																 #
#  - Suppose the number of total input files = 11				 #
#  - You wan to input maxium 4 input files for each run			 #													 
#	 >python excute.py input0 input1 input2 input3				 #
#    >python excute.py input4 input5 input6 input7				 #
#    >python excute.py input8 input9 input10	    			 #
#																 #
#  You can choose maxfile ( max input file number )			     #
#  The number of ouput files are automatically calculated		 #
##################################################################

file_list  = glob.glob("/xrootd_user/jwkim2/xrootd2/HEP_CNN_Large_Image/32PU/RPV/*.h5")
outfile_name = "outfile.h5"


def calc_Nout(maxfile,nfile):
	nfile = maxfile + nfile - 1
	nout = int(nfile / maxfile)
	return(nout)

maxfile=4 # Max number of input files for each run ( argumnet )
nfile=len(file_list) #  Number of total input files
nout  = calc_Nout(maxfile,nfile) # Number of output files


for i in range(nout):
	start = i*maxfile 
	end = start + maxfile 
	
	infiles = (' '.join(file_list[start:end]))

	fn = outfile_name.split('.')[0] 
	fn_out = fn + '_' + str(i) + ".h5"

	args = 'python' + ' '+ 'excute.py' + ' ' + '-option' + ' ' + fn_out + ' '+  infiles
	subprocess.call(args,shell=True)
