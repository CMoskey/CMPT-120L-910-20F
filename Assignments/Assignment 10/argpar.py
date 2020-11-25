import argparse
import logging
parser = argparse.ArgumentParser()

parser.add_argument("-sig", "--sigma", help="This will sum up all numbers in the array", action="store_true")
parser.add_argument("j", help="This number will print from one to the number")


args = parser.parse_args()

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def rollinglog(j):
    arr = []
    for n in range(j+1):
       arr.append(n)

    if args.sigma:
        b = sum(arr)
    return b
    
print(rollinglog(int(args.j)))