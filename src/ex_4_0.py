try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    
    with open(logfile, 'r') as file:
        
        database = file.read()
    
    shutdowning = list()
    
    for line in database.splitlines():
        
        if 'Shutdowning initiated' in line :
            
            shutdowning.append(line)
    
    return shutdowning
    


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
