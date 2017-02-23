

def init_data():
    with open('me_at_the_zoo.in', 'r') as f:
        header = f.readline().split()
        number_of_videos = header[0]
        endpoints = header[1]
        request_description = header[2]
        number_of_chache = header[3]

        dict_of_videos = {}
        i = 0
        videos_header = f.readline().split()
        for video in videos_header:
            dict_of_videos[i] = video
            i += 1

        print(dict_of_videos)
        # for i in range(0, len(lines)):
        #     line = lines[i]
        #     print(line)




    # return tmp.split()


def main():
    init_data()


if __name__ == '__main__':
    init_data()
