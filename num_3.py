def appearance(intervals: dict):
    lesson = intervals["data"]["lesson"]
    pupil = intervals["data"]["pupil"]
    tutor = intervals["data"]["tutor"]

    time_intervals = {
        'lesson_time': [],
        'pupil_time': [],
        'tutor_time': []
    }

    [time_intervals['lesson_time'].append(i) for i in range(lesson[0], lesson[1])]

    cnt = 0
    while cnt < len(pupil):
        for i in range(pupil[cnt], pupil[cnt + 1]):
            time_intervals['pupil_time'].append(i)
        cnt += 2

    cnt = 0
    while cnt < len(tutor):
        for i in range(tutor[cnt], tutor[cnt + 1]):
            time_intervals['tutor_time'].append(i)
        cnt += 2

    p = set(time_intervals['pupil_time'])
    t = set(time_intervals['tutor_time'])
    l = set(time_intervals['lesson_time'])

    l = l.intersection(t)
    l = l.intersection(p)

    return len(l)
