# ECOSTRESS-Sharpening-Tutorial

Tutorial for downscaling from ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) Land Surface Temperature to 20m using Sentinel-2 imagery.

If you are new with ECOSTRESS imagery and its basic image manipulations such as masking, first, visit the [ECOSTRESS Tutorials Repository](https://github.com/ECOSTRESS-Tutorials). It will introduce you to more basic steps and help you undertand what's done in these notebook.

The document called **"Setting_up_for_pyDMS.pdf"** explains the necessary steps to install the software environements and libraries to run the notebooks.

The folder named **"pyDMS_master"** contains the functions and classes necessary for the sharpening. You will have to make sure this is properly installed, as described in **"Setting_up_for_pyDMS.pdf"**. 

Once everything is installed, you'll be able to run both of the notebooks on your computer. **Sharpening_ECOSTRESS_S2.ipynb** will guide you to the downscaling of ECOSTRESS LST that you already have on your computer, whether it is from [AppEEARS](https://appeears.earthdatacloud.nasa.gov/), from [EarthDataSearch](https://search.earthdata.nasa.gov/search) or another source. **Sharpening_ECOSTRESS_S2_API.ipynb** will guide you to the downscaling of ECOSTRESS LST that you will download while running the notebook. You will only have to provide the Start and End dates for the imagery and a bounding box for the area of your choosing.

These notebooks are a wrap around [pyDMS](https://github.com/radosuav/pyDMS), developped by Guzinski and based off [Gao 2012]( https://doi.org/10.3390/rs4113287). This wrap makes the process of downscaling much easier and includes all the necessary preprocessing for downscaling ECOSTRESS LST with Sentinel-2 imagery.

The document called **"Common_sharpening_errors.pdf"** lists bugs/errors you might encounter when using the notebook and some ways to resolve these issues.

Even if there are some steps to ensure that we only downscale clear pixels. I adivse to check how the original granule looked, espicecially if the results is suspicious. It could be due to bad geolocation, unmasked clouds or any other error in the original image.

Questions, suggestions, or remarks: quentindehaene@gmail.com or glynn.hulley@jpl.nasa.gov, caroline.r.baumann@gmail.com
