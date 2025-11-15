#!/usr/bin/env python3
"""
Example usage of the photo manager tool

This script demonstrates various use cases for the photo manager.
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a command and print the description"""
    print(f"\n{'='*60}")
    print(f"Example: {description}")
    print(f"Command: {cmd}")
    print('='*60)
    
    result = subprocess.run(cmd, shell=True, capture_output=False)
    return result.returncode == 0

def main():
    print("Photo Manager - Usage Examples")
    print("=" * 60)
    
    # Check if photo_manager.py exists
    if not os.path.exists('photo_manager.py'):
        print("Error: photo_manager.py not found in current directory")
        sys.exit(1)
    
    examples = [
        {
            'desc': 'Show help information',
            'cmd': 'python photo_manager.py --help'
        },
        {
            'desc': 'Find duplicates in a directory (dry run)',
            'cmd': 'python photo_manager.py -d /path/to/photos --find-duplicates'
        },
        {
            'desc': 'Find duplicates in multiple directories',
            'cmd': 'python photo_manager.py -d /path/to/photos1 /path/to/photos2 --find-duplicates'
        },
        {
            'desc': 'Remove duplicates (dry run - preview only)',
            'cmd': 'python photo_manager.py -d /path/to/photos --remove-duplicates'
        },
        {
            'desc': 'Actually remove duplicates (BE CAREFUL!)',
            'cmd': 'python photo_manager.py -d /path/to/photos --remove-duplicates --execute'
        },
        {
            'desc': 'Organize photos by date (dry run)',
            'cmd': 'python photo_manager.py -d /path/to/photos --organize -o /path/to/organized'
        },
        {
            'desc': 'Actually organize photos by date',
            'cmd': 'python photo_manager.py -d /path/to/photos --organize -o /path/to/organized --execute'
        },
        {
            'desc': 'Find duplicates and organize by date in one command',
            'cmd': 'python photo_manager.py -d /path/to/photos --find-duplicates --organize -o /path/to/organized --execute'
        },
        {
            'desc': 'Enable verbose logging',
            'cmd': 'python photo_manager.py -d /path/to/photos --find-duplicates -v'
        }
    ]
    
    print("\nBelow are example commands. Replace /path/to/photos with your actual directory path.\n")
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['desc']}")
        print(f"   $ {example['cmd']}")
    
    print("\n" + "="*60)
    print("IMPORTANT SAFETY NOTES:")
    print("="*60)
    print("1. All operations run in 'dry run' mode by default")
    print("2. Add --execute flag to actually modify files")
    print("3. Always review the dry run output before using --execute")
    print("4. Back up your photos before removing duplicates!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
