#########################################################
###                                                   ###
###                    Utilities                      ###
###                                                   ###
#########################################################


import math
import os
import random


class UTIL():


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def ll_size(self, list_list):
        return len(list_list), len(list_list[0])
    

    def set_vector(self, res):
        vecs = []
        for i in range(res):
            for j in range(res):
                vecs.append((i, j))
        return vecs


    def pt2d_add(self, pt, vec):
        return (pt[0] + vec[0], pt[1] + vec[1])

    
    def get_number_of_files(self, dir_):
        return len(os.listdir(dir_))