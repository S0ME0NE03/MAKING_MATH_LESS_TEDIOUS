import datetime

def run_test():
    n = 0
    while n < limit:
        n +=1
        print(n)

def main():
    while True:
        action = input("Enter command (run test) (quit): ").lower().strip()
        if action == "quit":
            quit()
        
        elif action == "run test":
            start_time = datetime.datetime.now()
            run_test()
            end_time = datetime.datetime.now()

            time_interval = end_time - start_time
            print(time_interval)

if __name__ == "__main__":
    print("---Welcome to the python benchmarker---")
    limit = 10000000

    main()
