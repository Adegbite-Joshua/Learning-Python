from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())

    a = Process(target=counter, args=(50000,))
    b = Process(target=counter, args=(50000,))
    
    # a.start()
    # b.start()
    
    # b.join()
    # a.join()

    print('finished in:', time.perf_counter(), 'seconds')

if __name__ == "__main__":
    main()