# Medimsight aid diagnosis app
# Author: Medimsight Team
# Name: Medimsight Helloworld

mdsutil.logging("Initializing...")

#import mylibrary

# Get input
imagepath = mdsutil.get_input("vol_grp_t1")

# Input quality control
#mylibrary.checkinputquality(image)
mdsutil.logging("All inputs OK")

# Analysis
#results = mylibrary.runanalysis(image) OR
import itk

imageType = itk.Image[itk.F, 3]

def loadDICOM(path):
    readerType = itk.ImageSeriesReader[imageType]
    reader = readerType.New()

    ImageIOType = itk.GDCMImageIO
    dicomIO = ImageIOType.New()

    reader.SetImageIO(dicomIO)

    NamesGeneratorType = itk.GDCMSeriesFileNames
    nameGenerator = NamesGeneratorType.New()
    nameGenerator.SetUseSeriesDetails( True )
    nameGenerator.SetDirectory( path )

    seriesUID = nameGenerator.GetSeriesUIDs()
    fileNames = nameGenerator.GetFileNames ( seriesUID[0] )
    reader.SetFileNames( fileNames )

    reader.Update()

    return reader.GetOutput()

def writeNii(name, image):
    writer = itk.ImageFileWriter[image.GetPixel.im_class].New()
    writer.SetFileName('./' + name)
    writer.SetInput(image)
    writer.Update()


myImage = loadDICOM(imagepath)

medianFilterType = itk.MedianImageFilter[imageType, imageType]
medianFilter = medianFilterType.New()
medianFilter.SetInput(myImage)

writeNii("median.nii.gz", medianFilter.GetOutput())

# Output quality control
#mylibrary.checkoutputquality(results)
mdsutil.logging("All outputs OK")

# Set biomarkers
# Biomarker can be set to the patient directly from here use:
# name, value, original image, unit
#mdsutil.set_tag('Amazing Biomarker', results.value, image, 'mm')

# Set output
mdsutil.set_output("median", "./median.nii.gz")
mdsutil.logging("Finish")