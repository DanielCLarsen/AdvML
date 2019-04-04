import sys
from datetime import datetime
import time

class progress_bar(object):

    def __init__(self,max,length=50,title=None):
        self.max = max
        self.length = length
        self.counter = 0
        self.interval = int(max/length)
        self.progress = 0
        self.title = title
        self.start_time = time.time()
        self.setup()



    def __call__(self):
        self.counter+=1
        if self.counter % 1000 == 0:
            percent_tag = "{000:.2f}%".format((self.counter / self.max)*100)
            sys.stdout.write("%s]" % (" " * (self.length - self.progress)))
            sys.stdout.write(percent_tag)
            sys.stdout.flush()
            if self.counter != self.max:
                sys.stdout.write("\b" * (self.length + 1 - self.progress + len(percent_tag)))
            else:
                self.end()

        if self.counter % self.interval == 0:
            sys.stdout.write("#")
            self.progress += 1

    def setup(self):
        if self.title:
            print("\n"+self.title)
        sys.stdout.write("[%s]" % (" " * self.length))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.length + 1))
    def end(self):
        elapsed_time = datetime.fromtimestamp(time.time() - self.start_time)
        sys.stdout.write("  {}".format(elapsed_time.time()))
        sys.stdout.flush()