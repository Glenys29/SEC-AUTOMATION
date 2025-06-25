import time

def tail_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 0)  # Start to read the logs from the begining of the file
        for line in file:
            yield line # yield each line as it is read
        while True:
            line = file.readline() # read the next line
            if line:
                yield line # yield the next line if it is not empty
            else:
                time.sleep(0.5)
