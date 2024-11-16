#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def convert_to_sixel(input_path):
    """Convert a jpg file to sixel format"""
    output_path = input_path.with_suffix('.six')
    try:
        # Run img2sixel and redirect output to file
        with open(output_path, 'w') as f:
            subprocess.run(['img2sixel', str(input_path)], stdout=f, check=True)
        print(f"Converted: {input_path.name} -> {output_path.name}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path.name}: {e}")

def main():
    # Get current directory
    current_dir = Path('.')
    
    # Find all jpg files
    jpg_files = list(current_dir.glob('*.jpg'))
    jpg_files.extend(current_dir.glob('*.jpeg'))
    
    print(f"Found {len(jpg_files)} jpg files")
    
    # Convert each file
    for jpg_file in jpg_files:
        convert_to_sixel(jpg_file)

if __name__ == "__main__":
    main()