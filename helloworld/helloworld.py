# Medimsight aid diagnosis app
# Author: Medimsight Team
# Name: Medimsight Helloworld

mdsutil.logging("Initializing...")

#import mylibrary

# Get input
image = mdsutil.get_input("vol_grp_t1")

# Input quality control
#mylibrary.checkinputquality(image)
mdsutil.logging("All inputs OK")

# Analysis
#results = mylibrary.runanalysis(image)

# Output quality control
#mylibrary.checkoutputquality(results)
mdsutil.logging("All outputs OK")

# Set biomarkers
# Biomarker can be set to the patient directly from here use:
# name, value, original image, unit
#mdsutil.set_tag('Amazing Biomarker', results.value, image, 'mm')

# Set output
#mdsutil.set_output("pseudo_ct", results.image)
mdsutil.logging("Finish")