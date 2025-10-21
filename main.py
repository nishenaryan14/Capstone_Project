#!/usr/bin/env python3
"""
Banking Application - Main Launcher
Organized Banking Application with Python & SQL Implementation
"""

import sys
import os

def main():
    """Main launcher function"""
    try:
        # Add src/python to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_python_dir = os.path.join(current_dir, 'src', 'python')
        sys.path.insert(0, src_python_dir)
        
        # Import and run the main menu
        from main_menu import main as run_main_menu
        run_main_menu()
        
    except ImportError as e:
        print(f"❌ Error importing main menu: {e}")
        print("Make sure the src/python directory contains the required modules.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()

