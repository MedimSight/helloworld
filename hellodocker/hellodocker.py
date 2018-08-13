# Medimsight aid diagnosis app
# Author: Medimsight Team
# Name: Medimsight Hellodocker

mdsutil.logging("Initializing...")

#import mylibrary

# Get input
image = mdsutil.get_input("imageone")

# Input quality control
#mylibrary.checkinputquality(image)
mdsutil.logging("All inputs OK")

# Analysis
import glob
dicomfile = glob.glob(image + "/*")[0]

import pydicom as dicom
dfile = dicom.read_file(dicomfile) 
seriesd = dfile['0008', '103E'].value

import subprocess
mkdir = "docker pull ubuntu"
out, err = subprocess.Popen(mkdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
if err != '':
	raise Exception (out,err)
    
mkdir = "docker run -v $(pwd):/tmpexec ubuntu:latest /bin/sh -c \"echo 'write " + seriesd + " to txt' >> /tmpexec/pathtomytxt.txt;echo 'write, to, csv' >> /tmpexec/pathtomycsv.csv\""
out, err = subprocess.Popen(mkdir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
if err != '':
	raise Exception (out,err)

# or use DOCKER-PY. 
# Try with you own docker container!!
# Returning maps and images in DICOM or NIFTI is really cool as well.

#results = mylibrary.runanalysis(image)

# Output quality control
#mylibrary.checkoutputquality(results)
mdsutil.logging("All outputs OK")

# Set biomarkers
# Biomarker can be set to the patient directly from here use:
# name, value, original image, unit
#mdsutil.set_tag('Amazing Biomarker', results.value, image, 'mm')

# Set output
mdsutil.set_output("txtreport", './pathtomytxt.txt')
mdsutil.set_output("csvreport", './pathtomycsv.csv')

mdsutil.logging("Finish")


