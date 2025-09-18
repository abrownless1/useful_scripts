# Code to be used to plot xvg output files, typically from Gromacs #

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

def tuple_type(arg):
    try:
        parsed_tuple = tuple(int(x) for x in arg.split(','))
        return parsed_tuple
    except ValueError:
        raise argparse.ArgumentTypeError("Column values must be integers separated by columns")

def collect_axes_information(input_file):
    with open(input_file, 'r') as FILE:
        lines = FILE.readlines()
    for line in lines:
        if 'title' in line:
            print(line.split('title'))
            title = line.split('title')[1].replace('"','').replace('\n','')
        elif 'xaxis' in line:
            print(line.split('label'))
            xaxis = line.split('label')[1].replace('"','').replace('\n','')
        elif 'yaxis' in line:
            yaxis = line.split('label')[1].replace('"','').replace('\n','')
    return (title, xaxis, yaxis)

def plot_xvg(input_file, output_file, cols_of_interest):
    print(cols_of_interest)
    title, xaxis, yaxis = collect_axes_information(input_file)

    data = np.loadtxt(input_file, unpack=True, comments=['@','#'])

    
    fig = plt.figure(figsize=(4,3), tight_layout=True)
    plt.plot(data[cols_of_interest[0]], data[cols_of_interest[1]]) 
    plt.xlabel(xaxis)  #Change time units as needed
    plt.ylabel(yaxis)
    plt.title(title)
    fig.savefig(output_file, dpi=200)
    plt.close()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to plot xvg files using matplotlib')
    parser.add_argument('--input', type=str, help='Input file', required=True)
    parser.add_argument('--output', type=str, help='Output name', default='output.png')
    parser.add_argument('--columns_of_interest', type=tuple_type, help='If multiple columns are present in xvg file, denote columns of interest to be plotted in 2D in format x,y', default=(0,1))
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    plot_xvg(args.input, args.output, args.columns_of_interest)    
