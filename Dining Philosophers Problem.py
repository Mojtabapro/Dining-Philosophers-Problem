import threading
import time
import random


NUM_PHILOSOPHERS = 5

forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]
def philosopher(phil_id):
    left_fork = forks[phil_id]
    right_fork = forks[(phil_id + 1) % NUM_PHILOSOPHERS]

    while True:

        print(f"فیلسوف {phil_id} در حال فکر کردن است.")
        time.sleep(random.uniform(1, 3.5))

        print(f"فیلسوف {phil_id} گرسنه است.")


        first_fork, second_fork = \
            (left_fork, right_fork) \
                if phil_id % 2 == 0 else \
                (right_fork, left_fork)


        with first_fork:
            print(f"فیلسوف {phil_id} چنگال اول را برداشت.")
            with second_fork:
                print(f"فیلسوف {phil_id} چنگال دوم را برداشت و در حال خوردن است.")
                time.sleep(random.uniform(1, 1.5))
                print(f"فیلسوف {phil_id} غذا خوردن را تمام کرد.")

if __name__ == '__main__':
    threads = []
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    #run for forever
    for t in threads:
        t.join()
