#!/usr/bin/env python3
"""
Banking Application Launcher
Simple launcher for the Banking Application menu system
"""

import sys
import os

def main():
    """Main launcher function"""
    try:
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        
        # Import and run the main menu
        from .main_menu import main as run_main_menu
        run_main_menu()
        
    except ImportError as e:
        print(f"❌ Error importing main menu: {e}")
        print("Make sure main_menu.py is in the same directory.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
