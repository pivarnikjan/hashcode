#!/usr/bin/env python

import operator


def random(endpoint_cache, reqs, vids, cache, dc_lat):
    # vids = {k: v for k, v in vids.items() if v <= cache}

    # for
    # lines = 

    # with open('file_out', 'w') as file_out:
    #     file_out.write()
    pass


def store_vids(endpoint_cache, reqs, vids, cache, dc_lat):
        #      endpoint_cache: dict {int (cache): int (latency)}
        #      reqs:           dict {int (endpoint): int (number)}
        #      vids:           dict {int (vid#): int (size)}
        #      cache:          int (size of cache)
        #      dc_lat:         dict {int (endpoint): int (latency)}
    vids = {k: v for k, v in vids.items() if v <= cache}

    # reqs = {k: v for k, v in reqs.items() if k in vids.keys()}

    endpoint_cache_update = {}
    ep = 0
    for d_lat in dc_lat:
        # dc_lat = {k: v for k, v in vids.items() if v > cache}
        ec_update = {}
        for cid, c_lat in endpoint_cache[ep].items():
            if d_lat > c_lat:
                ec_update[cid] = c_lat
        endpoint_cache_update[ep] = ec_update
        ep += 1

    endpoint_cache = endpoint_cache_update

    reqs = sort_by_second(reqs)

    ans = itr_over(endpoint_cache, vids, reqs, dc_lat)

    return ans


def sort_by_second(reqs):
    return sorted(reqs, key=lambda x: x[2])


def itr_over(endpoint_cache, vids, reqs, dc_lat):
    # mx_ind = max(reqs, key=lambda i: reqs[i])

    list_ep_cache = sorted_dif_lat(endpoint_cache, dc_lat)
    ans = {}

    for ep, cache in list_ep_cache:
        for vid, epr, count in reqs:
            if ep == epr:
                ans[ep].append(vid)
                break

    # return c_max_dif_lat
    return ans


def find_pass(dict, mx):
    res = {}
    for k, v in dict:
        if v < mx:
            res[k] = v

    return res


def sorted_dif_lat(endp_cache, dc_lat):
    mx = 0
    mxc = -1
    emx = -1

    print(endp_cache)
    ekeys = endp_cache.keys()
    # dkeys = dc_lat.keys()

    res = []

    while ekeys != []:
        # ekeys = endp_cache.keys()

        for e in ekeys:
            dlat = dc_lat[e]

            # print(endp_cache[e])
            for k, v in endp_cache[e].items():
                if (dlat-v) > mx:
                    mx = dlat-v
                    mxc = k
                    emx = e

        del endp_cache[e][mxc]
        res.append((emx, mxc))

    return res
