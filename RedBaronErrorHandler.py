# Error Handling
import RedBaron
from redbaron import main_loop
def run_with_error_handling(func):
    try:
        func()
    except Exception as e:
        print(f"Error: {e}")
        main_loop()
