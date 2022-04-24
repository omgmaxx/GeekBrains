import os


def read_input(file):
    stat = {}
    stats = open(os.path.abspath(file), 'r')
    scr_floor = int(stats.read(3))
    for i in stats:
        i = i.split()
        stat[i[0], i[1]] = int(i[2])
    stats.close()
    return scr_floor, stat


def sorting_stats(floor, i_stats):
    stats = {}
    for i_name, i_score in i_stats.items():
        if i_score > floor:
            stats[i_name[0], i_name[1][:1] + '.'] = i_score
    stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
    return stats


def writing_stats(file, stats):
    output_results = open(os.path.abspath(file), 'w')

    cnt = 0
    output_results.write(f'{len(stats)}\n')
    for line in stats:
        cnt += 1
        output_results.write('{0}) {1} {2} {3}\n'.format(
            cnt,
            line[0][1],
            line[0][0],
            line[1])
        )
    output_results.close()


input_file = 'first_tour.txt'
output_file = 'second_tour.txt'

score_floor, statistics = read_input(input_file)
statistics = sorting_stats(score_floor, statistics)
writing_stats(output_file, statistics)
