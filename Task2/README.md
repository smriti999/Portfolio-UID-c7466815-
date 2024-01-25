Cat Shelter Log Analyzer


This Python script is designed to analyze a log file containing information about cat visits to a cat shelter. The purpose is to gain insights into the 
shelter's usage, particularly focusing on the behavior of the owner's cat ('OURS') and any intruding cats ('THEIRS'). The analysis includes metrics such
as the total number of visits, the number of intruding cats doused with water, and various duration statistics for the owner's cat.



Usage

-Ensure you have Python installed on your system. The script is executed from the command line and takes a log file path as an argument.
python cat_shelter.py <log_file_path>



Example

-python cat_shelter.py shelter_2023-08-25.log



Log File Format

-The log file should adhere to the following format, with each line representing a cat activity:

sql

OURS,600,630
THEIRS,700,701
OURS,842,900
THEIRS,1000,1001
THEIRS,1010,1011
END

-The first field indicates the cat type ('OURS' or 'THEIRS').

-The second and third fields represent entry and exit times in minutes from midnight.

-The log ends with the 'END' keyword.



Analysis Results

The script calculates and displays the following information:

-Cat Visits: Total number of visits by the owner's cat.

-Intruding Cats Doused: Number of intruding cats doused with water.

-Total Time in House: Cumulative time the owner's cat spent in the shelter.

-Average Visit Length: Average duration of each visit by the owner's cat.

-Longest Visit: Duration of the longest visit by the owner's cat.

-Shortest Visit: Duration of the shortest visit by the owner's cat.



Error Handling

-The script provides robust error handling for common issues related to command-line arguments, such as missing arguments or files that cannot be opened.
