import glob2
from datetime import datetime

filenames = glob2.glob("/beyond_basics/content_folder/*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "w") as mymerge:
    for filename in filenames:
        with open(filename, "r") as f:
            mymerge.write(f.read() + "\n")
