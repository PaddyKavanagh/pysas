#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author: Patrick Kavanagh (DIAS)
#
"""
functions relating to the loading of SAS and SAS related env variables.

:History:
26 Aug 2019: Created

"""
import constants
import subprocess

def source_sas():
    """
    Function to source SAS and HEADAS dependency
    """
    # source HEADAS
    headas_init = os.path.join(HEADAS_LOC, 'headas-init.bash')
    subprocess.Popen(subprocess.Popen(['source', headas_init]), shell=True)

    # source SAS
    sas_init = os.path.join(SAS_LOC, 'setsas.bash')
    subprocess.Popen(subprocess.Popen(['source', sas_init]), shell=True)

    return


