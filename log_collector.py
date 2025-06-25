import time

def tail_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 0)  # Start at the top
        for line in file:
            yield line
        while True:
            line = file.readline()
            if line:
                yield line
            else:
                time.sleep(0.5)
