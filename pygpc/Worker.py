#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 This is a wrapper script to be calles by the 'multiprocecsing.map' function in 'reg_adaptive'

@author: Benjamin Kalloch
"""
import time
import numpy as np

def init(queue):
    """
    This function will be called upon inititalization of the process.
    It sets a global variable denoting the ID of this process that can
    be read by any function of this process

    Parameters
    ----------
    queue : multiprocessing.Queue
             the queue object that manages the unique IDs of the process pool
    """
    global process_id
    process_id = queue.get()

def run(obj):
    """
    This is the main worker function of the process.
    Methods of the provided object will be called here.

    Parameters
    ----------
    obj : any callable object
           The object that
                a) handles the simulation work
                b) reading previous results
                c) writing the calculated result fields
                d) printing global process
    """
    global process_id

    if process_id is None:
        process_id = 0

    res = obj.read_previous_results()

    start_time = 0
    end_time   = 0
    skip_sim   = True

    # skip if there was no data row for that i_grid or if it was prematurely inserted (= all zero)
    if res is None or not np.any( res ):
        start_time = time.time()
        res = obj.simulate(process_id)
        end_time = time.time()
        obj.write_results(res)
        skip_sim = False

    obj.increment_ctr()
    obj.print_progress(func_time=end_time - start_time, read_from_file=skip_sim);

    return ( obj.get_seq_number(), res)