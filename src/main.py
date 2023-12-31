# THe main file for the Fourier Analysis project will extract the arguments from the command line
# and call the appropriate function to perform the desired operation. Command line arguments will be:
# -h --help for help
# -s --syntax for function string syntax guide
# -f --function for function string (cannot be invoked if -c or -i is used)
# -c --csv for csv file (Optional if -i is used, cannot be invoked with -f)
# -i --input for function string file (optional if -c is used, cannot be invoked with -f)
# -ift --inverse-fourier-transform for inverse fourier transform
# -fft --fast-fourier-transform or fast fourier transform
# (-ift or -fft is required)
# -o for output file name (Optional if -f, Required for -c and -i)
# -v [2D|3D] for visualization of the result

import sys
import argparse
from Physics.Fourier_Analysis.src.lexer import lex_func, lex_csv
from Physics.Fourier_Analysis.src.parser import parse_func
from Physics.Fourier_Analysis.src.fourier import ift
from Physics.Fourier_Analysis.src.fourier import fft
from Physics.Fourier_Analysis.src.visualization import visualization

def main():
    parser = argparse.ArgumentParser(description='Fourier Analysis')
    parser.add_argument('-s', '--syntax', action='store_true', help='Prints out the function string syntax guide')
    parser.add_argument('-f', '--function', type=str, help='Function string to perform IFT or FFT on')
    parser.add_argument('-c', '--csv', type=str, help='CSV file to perform IFT or FFT on')
    parser.add_argument('-i', '--input', type=str, help='File containing function strings to perform IFT or FFT on')
    parser.add_argument('-ift', '--inverse-fourier-transform', action='store_true', help='Perform inverse fourier transform')
    parser.add_argument('-fft', '--fast-fourier-transform', action='store_true', help='Perform fast fourier transform')
    parser.add_argument('-o', '--output', type=str, help='Output file name')
    parser.add_argument('-v', '--visualization', type=str, help='Visualization of the result')

    args = parser.parse_args()
    


