#!/usr/bin/env python3.11
import sys
import textstat

def calculate_readability(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    score = textstat.flesch_reading_ease(content)
    print(f'Flesch-Kincaid Reading Ease: {score}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3.11 calculate_readability.py <file_path>')
        sys.exit(1)
    
    file_path = sys.argv[1]
    calculate_readability(file_path)
