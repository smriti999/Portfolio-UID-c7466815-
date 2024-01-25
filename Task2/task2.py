import sys
from datetime import timedelta

def analyze_cat_shelter_log(log_file_path):
    # Initialize variables
    cat_visits = 0
    intruding_cats_doused = 0
    total_time_in_house = 0
    longest_visit = 0
    shortest_visit = float('inf')

    # Read and process the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            # Split the line into fields using ',' as the delimiter
            fields = line.strip().split(',')
            
            if len(fields) == 3:
                # Extract relevant information from the fields
                cat_type, entry_time, exit_time = fields
                entry_time, exit_time = int(entry_time), int(exit_time)
                visit_duration = exit_time - entry_time
                
                # Check if the cat is 'OURS' or 'THEIRS' and update variables accordingly
                if cat_type == 'OURS':
                    cat_visits += 1
                    total_time_in_house += visit_duration

                    # Update longest and shortest visit durations
                    if visit_duration > longest_visit:
                        longest_visit = visit_duration

                    if visit_duration < shortest_visit:
                        shortest_visit = visit_duration
                elif cat_type == 'THEIRS':
                    # Count the number of intruding cats doused with water
                    intruding_cats_doused += 1

    # Calculate average visit length
    if cat_visits > 0:
        average_visit_length = total_time_in_house / cat_visits
    else:
        average_visit_length = 0

    # Format time durations into human-readable strings
    total_time_formatted = str(timedelta(minutes=total_time_in_house))
    longest_visit_formatted = str(timedelta(minutes=longest_visit))
    shortest_visit_formatted = str(timedelta(minutes=shortest_visit))
    average_visit_length_formatted = str(timedelta(minutes=average_visit_length))

    # Display analysis results
    print("\nLog File Analysis")
    print("==================\n")
    print(f"Cat Visits: {cat_visits}")
    print(f"Intruding Cats Doused: {intruding_cats_doused}")
    print(f"\nTotal Time in House: {total_time_formatted}")
    print(f"\nAverage Visit Length: {average_visit_length_formatted}")
    print(f"Longest Visit:        {longest_visit_formatted}")
    print(f"Shortest Visit:       {shortest_visit_formatted}")

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python cat_shelter.py <log_file_path>")
    sys.exit(1)

# Get the log file path from the command line arguments
log_file_path = sys.argv[1]

try:
    # Call the function to analyze the cat shelter log
    analyze_cat_shelter_log(log_file_path)
except FileNotFoundError:
    print(f'Cannot open "{log_file_path}"!')
