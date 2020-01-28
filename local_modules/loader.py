# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:57:06 2020

@author: mhader
"""


import os

def load_data(path):

    """

    Load dataset

    """

    input_file = os.path.join(path)

    with open(input_file, "r", encoding='utf-8') as f:

        data = f.read()



    return data.split('\n')
