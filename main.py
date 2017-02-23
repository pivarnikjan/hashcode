
def parse_datacenter_lat_number_of_caches(row):
    return row[0], row[1]


def init_data():
    with open('me_at_the_zoo.in', 'r') as f:
        header = f.readline().split()
        number_of_videos = header[0]
        endpoints = header[1]
        request_description = header[2]
        number_of_chache = header[3]
        cache_mem = header[4]

        # 1


        # 2


        # 3
        vids = {}
        i = 0
        videos_header = f.readline().split()
        for video in videos_header:
            vids[i] = video
            i += 1
        print(vids)

        # 4
        cache = (number_of_chache, cache_mem)

        # 5

        return (endpoint_cache, reqs, vids, cache, dc_lat)


def main():
    init_data()


if __name__ == '__main__':
    init_data()
