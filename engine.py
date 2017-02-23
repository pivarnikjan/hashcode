#!/usr/bin/env python

import operator

def store_vids(endpoint_cache, reqs, vids, cache, dc_lat):
        #      endpoint_cate: dict {int (cache): int (latency)}
        #      reqs:           dict {int (endpoint): int (number)}
        #      vids:           dict {int (vid#): int (size)}
        #      cache:          int (size of cache)
        #      dc_lat:         dict {int (endpoint): int (latency)}
    vids = {k: v for k, v in vids.items() if v <= cache}

    reqs = {k: v for k, v in reqs.items() if k in vids.keys()}

    endpoint_cache_update = []
    for ep, d_lat in dc_lat:
        # dc_lat = {k: v for k, v in vids.items() if v > cache} 
        ec_update = {}
        for ec in endpoint_cache:
            for cid, c_lat in d_lat:
                if d_lat > c_lat:
                    ec_update[cid] = c_lat
        endpoint_cache_update.append(ec_update)

    endpoint_cache = endpoint_cache_update

    
def itr_over(endpoint_cache, vids):
    pass


def find_pass(dict, mx):
    res = {}
    for k, v in dict:
        if v < mx:
            res[k] = v

    return res
