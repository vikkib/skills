#!/usr/bin/env python3.11
import sys
import re

def count_keywords(file_path, keywords):
    with open(file_path, 'r') as f:
        content = f.read().lower()
    
    for keyword in keywords:
        count = len(re.findall(r'\b' + keyword.lower() + r'\b', content))
        print(f'{keyword}: {count}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3.11 keyword_checker.py <file_path> <keyword1> <keyword2> ...')
        sys.exit(1)
    
    file_path = sys.argv[1]
    keywords = sys.argv[2:]
    count_keywords(file_path, keywords)
