import sys
import csv

def help():
    print('Usage: {} <input_file> [output_file]'.format(sys.argv[0]))


def convert_to_fastq(in_file, out_file):
    # throw away the first line (with headings)
    in_file.readline()
    reader = csv.reader(in_file)
    
    for line in reader:
        for i, col in enumerate(line):
            out_file.write(col + '\n')
            if i == 1:
                out_file.write('+\n')

def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    else:
        in_file = sys.argv[1]
        if len(sys.argv) >= 3:
            # If we have it, take name of output from parameters
            out_file = sys.argv[2]
        else:
            # else make it from input file name
            out_file = '.'.join(in_file.split('.')[:-1]) + '.fastq'

        with open(in_file) as infd:
            with open(out_file, 'w') as outfd:
                convert_to_fastq(infd, outfd)


if __name__ == '__main__':
    main()
