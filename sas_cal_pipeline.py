#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author: Patrick Kavanagh (DIAS)
#
"""
functions for running the SAS calibration pipelines

:History:
26 Aug 2019: Created

"""
import os
import glob
import constants
import subprocess

def run_cifbuild_odfingest(ccf_dir, odf_dir):
    """
    Function to run cifbuild and odfingest
    """
    # cifbuild
    sas_ccf = os.path.join(ccf_dir, 'ccf.cif')

    cmd = ['cifbuild', 'withccfpath=no', 'analysisdate=now', 'category=XMMCCF',
           'calindexset={}'.format(sas_ccf), 'fullpath=yes']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
    print p.returncode

    # odfingest
    cmd = ['odfingest', 'odfdir={}'.format(odf_dir), 'outdir={}'.format(odf_dir)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
        print line
    p.wait()
    print p.returncode

    odf_file = glob.glob(os.path.join(odf_dir, '*.SAS'))[0]

    # set the environment variables for SAS
    os.environ['SAS_CCF'] = sas_ccf
    os.environ['SAS_ODF'] = odf_file
    os.environ['SAS_CCFPATH'] = CCF_LOC

    return


