from os import read
import sys
import datetime as dt
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def run(args=None):
    print(bcolors.OKCYAN)
    print("\n|''''''''''''''''''''''''''''''''''''''''|")
    print("| Starting subtitles shifter aplication. |")
    print("|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|","\n")

    
    try:
        file = open(args.input_file,"r",encoding='utf-8-sig')    
        print(bcolors.OKBLUE)
        print("|''''''''''''''''''''''''''''''''''''''''''''")
        print("| Selected file: ", args.input_file , "          ")
    except IOError: 
        print(bcolors.FAIL +"| Error: Subtitles file couldn't be oppened. "+ bcolors.FAIL)
        return
    
    seconds = float(args.time)
    print("| Subtitles will be shifted by", args.time , "seconds   ")

    temp = file.read()
    temp = temp.strip().split("\n\n")

    file.close()

    subs = []
    for line in temp:
        line = line.split("\n")
        subs.append(line)


    def forwardShift(time,secs):
        time = dt.datetime.strptime(time, '%H:%M:%S,%f')
        mod_time = (time + dt.timedelta(seconds=secs)).strftime('%H:%M:%S,%f')
        return mod_time[:-3]

    def backwardShift(time,secs):
        time = dt.datetime.strptime(time, '%H:%M:%S,%f')
        mod_time = (time - dt.timedelta(seconds=secs)).strftime('%H:%M:%S,%f')
        return mod_time[:-3]

    print("| Selected mode:", args.mode ,"                    ")
    print("| Selected range:", args.range ,"                    ")
    print("|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,," +"\n")

    print(bcolors.OKGREEN)
    print("|''''''''''''''''''''''''''''''''''''''''''''")
    print("|Shifted from:                               ")
    print("|", subs[0][1] ,"             ")
    print("|To:                                         ")

    subs_range = args.range
    for l in subs:
        if int(l[0]) >= subs_range[0] and int(l[0]) <= subs_range[1]:
            if args.mode == "forward":
                time1 = forwardShift(l[1][:12],seconds)
                time2 = forwardShift(l[1][17:29],seconds)
            elif args.mode == "backward":
                time1 = backwardShift(l[1][:12],seconds)
                time2 = backwardShift(l[1][17:29],seconds)
            l[1] = f"{time1} --> {time2}"
    print("|", subs[0][1] ,"             " )
    print("|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
    subs_file = open(args.output_file,"w")
    subs_file.truncate()
    for sub in subs:
        for line in sub:
            subs_file.write(f"{line}\n") 
        subs_file.write("\n")
    subs_file.close()

    print(bcolors.WARNING)
    print("|''''''''''''''''''''''''''''''''''''''''''''")
    print("|Shifted subtitles were saved to: ",args.output_file,"  " )
    print("|,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
    print(bcolors.ENDC)

def parse_args():
    desc = """Subtitles Shifter
This is a small program that I wrote to help myself 
with the synchronization of subtitles in movies.

Check readme.md for example usage."""
    parser = argparse.ArgumentParser(description=desc,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i','--input_file', required=True, help="Path to the file with original subtitles.")
    parser.add_argument('-o','--output_file', required=True, help="Path to the file where shifted subtitles will be saved.")

    parser.add_argument('-m','--mode',help="Shift subtitles forward or backward. Usage: --mode forward/backward |Default: forward" , default="forward",type=str)

    parser.add_argument(
        '-t',
        '--time',
        help="Amount of time in seconds to shift the subtitles | Usage: --time 5.4 " ,
        type=float,
        default=1.0)
    
    parser.add_argument(
        '-r',
        '--range',
        nargs='+',
        help="The range you want the subtitles to be shifted (only two first numbers will be used) | Usage: --range 50 125 ",
        type=int,
        default=(1,10000))
    
    args = parser.parse_args()
    return args


def main():
    run(parse_args())
if __name__ == '__main__':
    main()

