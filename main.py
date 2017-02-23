#!/usr/bin/env python

from engine import store_vids

def parse_datacenter_lat_number_of_caches(row):
    return row[0], row[1]


def cache_latency(number_of_rows, file):
    endp_cache = {}
    for row in range(number_of_rows):
        tmp = file.readline().split()
        endp_cache[tmp[0]] = tmp[1]

    return endp_cache


def init_data():
    with open('me_at_the_zoo.in', 'r') as f:
        header = f.readline().split()
        number_of_videos = int(header[0])
        number_of_endpoints = int(header[1])
        request_description = int(header[2])
        number_of_chache = int(header[3])
        cache_mem = int(header[4])

        # 3
        vids = {}
        i = 0
        videos_header = f.readline().split()
        for video in videos_header:
            vids[i] = int(video)
            i += 1

        # 5
        dc_lat = []
        # 1
        endp_cache = []
        for i in range(number_of_endpoints):
            row = f.readline().split()
            dc_lat.append(row[0])
            endp_cache.append(cache_latency(number_of_rows=int(row[1]), file=f))
        # print(endp_cache)
        # print(dc_lat)

        # 2
        reqs = []
        # lines = f.readlines()
        lines = f.read().splitlines()
        for item in lines:
            reqs.append(item.split())
        # print(reqs)

        # 4
        cache = (number_of_chache, cache_mem)

        return (endp_cache, reqs, vids, cache, dc_lat)
        #      endpoint_cache: dict {int (cache): int (latency)}
        #      reqs:           dict {int (endpoint): int (number)}
        #      vids:           dict {int (vid#): int (size)}
        #      cache:          int (size of cache)
        #      dc_lat:         dict {int (endpoint): int (latency)}


def main():
    init_data()


if __name__ == '__main__':
    init_dat = init_data()
    print(init_dat)
    print(init_dat[0][0])
    store_vids(*init_dat)
