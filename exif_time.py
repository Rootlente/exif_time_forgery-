import os
import sys

def get_file_times(file):
    # Get the file stats
    stats = os.stat(file)

    # Convert the modification, access, and inode change times to nanoseconds
    mod_time_ns = stats.st_mtime * 1000000000
    acc_time_ns = stats.st_atime * 1000000000
    ino_time_ns = stats.st_ctime * 1000000000

    return (mod_time_ns, acc_time_ns, ino_time_ns)

# Get the file from the command-line argument
file = sys.argv[1]

# Test the function
mod_time_ns, acc_time_ns, ino_time_ns = get_file_times(file)

# Print the file times
print(f'Modification time: {mod_time_ns} nanoseconds')
print(f'Access time: {acc_time_ns} nanoseconds')
print(f'Inode change time: {ino_time_ns} nanoseconds')

