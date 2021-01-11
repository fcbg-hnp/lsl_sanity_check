#!/usr/bin/env python3
#coding:utf-8

"""
  Author: Arnaud Desvachez <arnaud.desvachez@gmail.com>
  Purpose: Check the recorded LSL streams' sanity.
  Created: 11.01.2021
"""
import os
import logging
import numpy as np

from pyxdf import load_xdf
from pathlib import Path

logger = logging.getLogger("lsl_sanity_logger")
logger.setLevel(logging.INFO)
hdlr = logging.StreamHandler()
hdlr.setLevel(logging.INFO)
logger.addHandler(hdlr)

# ------------------------------------------------------------------------------------------
def get_ch_info(stream):
    """
    Extract the info for each eeg channels (label, type and unit)
    """
    labels, types, units = [], [], []
    n_chans = int(stream["info"]["channel_count"][0])
    
    # Get channels labels, types and units
    if stream["info"]["desc"] and stream["info"]["desc"][0]:
        for ch in stream["info"]["desc"][0]["channels"][0]["channel"]:
            labels.append(str(ch["label"][0]))
            try:
                types.append(ch["type"][0])
                units.append(ch["unit"][0])
            except:
                pass
    
    if not labels:
        labels = ["Ch_" + str(n) for n in range(n_chans)]
    
    if not units:
        units = ["NA" for _ in range(n_chans)]    
    
    return labels, types, units    

# ------------------------------------------------------------------------------------------
def lsl_sanity_check(filename):
    """
    Check the recorded LS streams' sanity.
    """
    # ---------------------------------------------
    # Load the data 
    # ---------------------------------------------
    logger.info("-----------------------------------------------------")
    logger.info("Loading data from the xdf file: {}\n".format(filename))
    streams, _= load_xdf(filename)
    
    # ---------------------------------------------
    # Check the streams
    # ---------------------------------------------    
    for stream in streams:
        
        name = stream["info"]["name"][0]
        n_chans = int(stream["info"]["channel_count"][0])
        fs = float(stream["info"]["nominal_srate"][0])
        labels, types, units = get_ch_info(stream)
        
        logger.info("-----------------------------------------------------")
        logger.info("Found stream '{}' ({} channels, sampling rate {}Hz).".format(name, n_chans, fs))
        logger.info("Channels: {}".format(labels))        
        logger.info("Data shape: {}\n".format(np.array(stream["time_series"]).shape))
        logger.info(stream["time_series"])
        print("\n")
        
    logger.info("Done")
        

#----------------------------------------------------------------------
if __name__ == '__main__':

    filename = str(Path(input(">> Provide the path to the xdf file to process: \n")))
    
    if not os.path.isfile(filename):
        logger.info("The provided file {} does not exist".format(filename))
        raise IOError
    
    lsl_sanity_check(filename)

