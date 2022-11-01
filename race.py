import random
from datetime import datetime
from time import sleep

from track import Track
from cars import Car


def do_race():
    track = Track(random.randint(12, 24))
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    car1 = Car("X")
    car2 = Car("O")

    track.lane1[0] = car1.model
    track.lane2[0] = car2.model

    for race in range(len(track.lane1)):
        current_pos = track.lane1.index(car1.model)
        current_pos_2 = track.lane2.index(car2.model)

        next_pos = current_pos + car1.speed
        next_pos_2 = current_pos_2 + car2.speed

        track.lane1.pop(current_pos)
        track.lane2.pop(current_pos_2)

        track.lane1.insert(next_pos, car1.model)
        track.lane2.insert(next_pos_2, car2.model)

        print(*track.lane1, sep="")
        print(*track.lane2, sep="")
        sleep(1)
        if track.lane1[len(track.lane1) - 1] == car1.model \
                and track.lane2[len(track.lane2) - 1] == "|":
            track.lane1.clear()
            print(f"{car1.model} has won! \n Race finished ")
            with open("results.txt", "w") as results:
                results.write(f"{car1.model} has won at {time} \n")
            break
        elif track.lane2[len(track.lane2) - 1] == car2.model \
                and track.lane1[len(track.lane1) - 1] == "|":
            track.lane2.clear()
            print(f"{car2.model} has won! \n race finished ")
            with open("results.txt", "w") as results:
                results.write(f"{car2.model} has won at {time} \n")
            break
        elif track.lane1[len(track.lane1) - 1] == car1.model:
            print("TIE!")
            with open("results.txt", "w") as results:
                results.write(f" it is TIE at {time} \n ")
            break


