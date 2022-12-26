import time, sys, getopt


def main(argv):
    # TODO documentazione + spiegazione degl argomenti

    opts, args = getopt.getopt(argv, "Sh:m:s:", ["hours=", "minutes=", "seconds=", "show_all", "help"])
    hours = 0
    minutes = 0
    seconds = 0
    show_all = False

    for opt, arg in opts:
        if opt == '--help':
            print("help in here")  # TODO insert help
            sys.exit()
        elif opt in ("-S", "--show_all"):
            show_all = True
        elif opt in ("-h", "--hours"):
            hours = int(arg)
        elif opt in ("-m", "--minutes"):
            minutes = int(arg)
        elif opt in ("-s", "--seconds"):
            seconds = int(arg)

    initial_time_in_s = to_seconds(hours, minutes, seconds)
    remaining_time = initial_time_in_s

    print("Start timer: " + to_hms_format(remaining_time))
    tic = time.perf_counter()
    while remaining_time:
        # TODO questo controllo non rallenta il timer? se sì, di quanto?
        #  qualsiasi operazione, non impiega dei secondi?
        #  (verificare per tempi grandi: 5m con tutti gli output --> imprecisione ~ -0.34s)
        if show_all or remaining_time % 10 == 0 or remaining_time < 10:
            print(to_hms_format(remaining_time))
        time.sleep(1)  # sleep time 1 sec
        remaining_time -= 1
    print("0 -- STOP!")
    toc = time.perf_counter()
    print("".join(["TEST: imprecisione = ", str(initial_time_in_s-toc+tic)]))


def to_hms_format(total_in_seconds):
    hours = int(total_in_seconds / 360)
    minutes = int((total_in_seconds % 360)/60)
    seconds = int(total_in_seconds % 60)
    return "".join([str(hours), 'h', str(minutes), 'm', str(seconds), 's'])


def to_seconds(hours, minutes, seconds):
    initial_time_in_s = hours * 360 + minutes * 60 + seconds
    return initial_time_in_s


if __name__ == "__main__":
    main(sys.argv[1:])

