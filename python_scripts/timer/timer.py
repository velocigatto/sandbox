import time
import sys

#TODO add gestione migliore degli argomenti https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#TODO documentazione + spiegazione degl argomenti
#TODO aggiungere argomenti per ore, minuti, secondi tipo -H 1 -M 18 -S 4 (1h18'4'')
inital_time = int(sys.argv[1])
show_all = len(sys.argv) > 2 and sys.argv[2] == "all"


initial_time_in_s = inital_time
remaining_time = initial_time_in_s

while remaining_time:
    # TODO questo controllo non rallenta il timer? se sì, di quanto? anche stampare, non impiega dei secondi? (verificare per tempi grandi)
    if show_all or remaining_time % 10 == 0 or remaining_time < 10:
        print(remaining_time)
    time.sleep(1)  # sleep time 1 sec
    remaining_time -= 1
print("0 -- STOP!")
