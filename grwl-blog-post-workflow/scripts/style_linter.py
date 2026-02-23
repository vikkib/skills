#!/usr/bin/env python3.11
import sys
import subprocess

def lint_prose(file_path):
    try:
        result = subprocess.run(["proselint", "check", file_path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Proselint stderr:\n{result.stderr}")
    except FileNotFoundError:
        print("Error: 'proselint' command not found. Make sure it is installed and in your PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3.11 style_linter.py <file_path>')
        sys.exit(1)
    
    file_path = sys.argv[1]
    lint_prose(file_path)
