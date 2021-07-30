import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from core.managerSystem import StudentManager


if __name__ == '__main__':
    manager = StudentManager()
    manager.run()
