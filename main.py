def parse_datacenter_lat_number_of_caches(row):
    return row[0], row[1]


def cache_latency(number_of_rows, file):
    endp_cache = {}
    for row in range(number_of_rows):
        tmp = file.readline().split()
        endp_cache[int(tmp[0])] = int(tmp[1])

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
            dc_lat.append(int(row[0]))
            endp_cache.append(cache_latency(number_of_rows=int(row[1]), file=f))
        # print(endp_cache)
        # print(dc_lat)

        # 2
        reqs = []
        # lines = f.readlines()
        lines = f.read().splitlines()
        for item in lines:
            tmp = item.split()
            tmp_int = [int(int_num) for int_num in tmp]
            reqs.append(tmp_int)
        # print(reqs)

        # 4
        cache = (number_of_chache, cache_mem)

        return (endp_cache, reqs, vids, cache, dc_lat)
        #      endpoint_cache: dict {int (cache): int (latency)}
        #      reqs:           dict {int (endpoint): int (number)}
        #      vids:           dict {int (vid#): int (size)}
        #      cache:          int (size of cache)
        #      dc_lat:         dict {int (endpoint): int (latency)}


def _check_number_of_caches(file, number_of_lines):
    lines = len(file.readlines())
    return True if number_of_lines == lines else False


def _check_size_of_videos_in_caches(max_size, videos_len_sum):
    return True if max_size >= videos_len_sum else False


def _maximum_size(number_of_caches, cache_size):
    return number_of_caches*cache_size


def _indexes_of_videos(f):
    lines = f.read().splitlines()
    caches = []
    for item in lines:
        tmp = item.split()
        tmp.pop(0)
        caches += tmp
        # caches.append(item.split())
    return set(caches)


def _size_of_videos(f, vids):
    indexes = _indexes_of_videos(f)
    vids_len_sum = 0
    for cache in indexes:
        vids_len_sum += vids[int(cache)]
    return vids_len_sum


def validation(file):
    endp_cache, reqs, vids, cache, dc_lat = init_data()
    with open(file, 'r') as f:
        number_of_caches = int(f.readline())
        # _check_number_of_caches(f, number_of_caches)
        vids_size = _size_of_videos(f, vids)
        max_size = _maximum_size(number_of_caches, cache[1])
        tmp = _check_size_of_videos_in_caches(max_size=max_size, videos_len_sum=vids_size)
        print(tmp)

        # results = list(map(int, caches))
        # print(results)
        # return True if _check_number_of_caches(f, int(f.readline())) and _check_size_of_videos() else False


def main():
    # init_data()
    validation('validation_test.txt')


if __name__ == '__main__':
    main()
