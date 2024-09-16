# -*- coding: utf-8 -*-
"""
@author: radoslaw guzinski
Copyright: (C) 2017, Radoslaw Guzinski
"""
import os
import time

from osgeo import gdal

import pyDMS.pyDMSUtils as utils
from pyDMS.pyDMS import DecisionTreeSharpener, NeuralNetworkSharpener
from pyDMS.pyDMS import REG_sknn_ann, REG_sklearn_ann



# wv_tile_dir = r'C:\Users\qdehaene\Documents\Data\WV3\23APR07184157-M2AS-508246526040_01_P003'
# wv_tile_name = wv_tile_dir[-39:]
# wv_tile_path = os.path.join(wv_tile_dir,wv_tile_name) 
# wv_tif_path = wv_tile_path +'.tif'
# dump_path = r'C:\Users\qdehaene\Documents\Data\WV3 tiles cut hy'
# path = os.path.join(dump_path,wv_tile_name)
# path = path+'flight'+ str(0)+ '.tif'

# highResFilename = r'C:\Users\qdehaene\Documents\Data\HLS\LA\05-13-22\HLS_LA_rp_cropped.tif'
# lowResFilename = r'C:\Users\qdehaene\Documents\Data\ECOSTRESS\test\ECO2LSTE.001_SDS_LST_doy2022124081538_aid0001_scaled.tif'
# lowResMaskFilename = r"C:\Users\qdehaene\Documents\Data\ECOSTRESS\test\ECO2LSTE.001_SDS_QC_doy2022124081538_aid0001_QF.tif"
# outputFilename = r'C:\Users\qdehaene\Documents\Data\Sharpened LST\Sharpened ECOSTRESS\ECO2LSTE.001_SDS_LST_doy2022124081538_aid0001_scaled_sharp_mw.tif'

##########################################################################################

if __name__ == "__main__":

    lr_dir = r'C:\Users\qdehaene\Documents\Data\ECOSTRESS\SDS_LST\scaled'
    useDecisionTree = False
    hr_img_path = r'C:\Users\qdehaene\Documents\Data\HLS\LA\05-13-22\HLS_LA_rp.tif'
    QC_dir = r'C:\Users\qdehaene\Documents\Data\ECOSTRESS\QC'
    for file in os.listdir(lr_dir) :
        outputFilename = os.path.join(r'C:\Users\qdehaene\Documents\Data\Sharpened LST\Sharpened ECOSTRESS\pyDMS',file.replace('.tif','_sharp_pyDMS.tif'))
        
        highResFilename = hr_img_path #hr_path_list[j]
        lowResFilename = os.path.join(lr_dir,file) # lr_path_list[j]
        # print(lowResFilename)
        # file_qc = file.replace('LST','QC',)
        # file_qc = 'QC'.join(file.rsplit('LST', 1))
        # print(file_qc)
        # file_qf = file_qc.replace('.tif','_QF.tif')
        lowResMaskFilename = r'' #os.path.join(QC_dir,file_qf)
        commonOpts = {"highResFiles":               [highResFilename],
                        "lowResFiles":                [lowResFilename],
                        "lowResQualityFiles":         [lowResMaskFilename],
                        "lowResGoodQualityFlags":     [0],
                        "cvHomogeneityThreshold":     0,
                        "movingWindowSize":           0,
                        "disaggregatingTemperature":  True}
        dtOpts =     {"perLeafLinearRegression":    True,
                        "linearRegressionExtrapolationRatio": 0.25}
        sknnOpts =   {'hidden_layer_sizes':         (10,),
                        'activation':                 'tanh'}
        nnOpts =     {"regressionType":             REG_sklearn_ann,
                        "regressorOpt":               sknnOpts}

        start_time = time.time()

        if useDecisionTree:
            opts = commonOpts.copy()
            opts.update(dtOpts)
            disaggregator = DecisionTreeSharpener(**opts)
        else:
            opts = commonOpts.copy()
            opts.update(nnOpts)
            disaggregator = NeuralNetworkSharpener(**opts)

        print("Training regressor...")
        disaggregator.trainSharpener()
        print("Sharpening...")
        downscaledFile = disaggregator.applySharpener(highResFilename, lowResFilename)
        print("Residual analysis...")
        residualImage, correctedImage = disaggregator.residualAnalysis(downscaledFile, lowResFilename,
                                                                        lowResMaskFilename,
                                                                        doCorrection=True)
        print("Saving output...")
        highResFile = gdal.Open(highResFilename)
        if correctedImage is not None:
            outImage = correctedImage
        else:
            outImage = downscaledFile
        # outData = utils.binomialSmoother(outData)
        outFile = utils.saveImg(outImage.GetRasterBand(1).ReadAsArray(),
                                outImage.GetGeoTransform(),
                                outImage.GetProjection(),
                                outputFilename)
        residualFile = utils.saveImg(residualImage.GetRasterBand(1).ReadAsArray(),
                                        residualImage.GetGeoTransform(),
                                        residualImage.GetProjection(),
                                        os.path.splitext(outputFilename)[0] + "_residual" +
                                        os.path.splitext(outputFilename)[1])

        outFile = None
        residualFile = None
        downsaceldFile = None
        highResFile = None

        print(time.time() - start_time, "seconds")
