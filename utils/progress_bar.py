import sys
from datetime import datetime
import time

class progress_bar(object):

    def __init__(self, max_c, length=50, title=None):
        self.max_c = max_c
        self.length = length
        self.counter = 0
        self.interval = int(max_c / length)
        self.prct_update = int(self.interval/10)
        self.progress = 0
        self.title = title
        self.start_time = time.time()
        self.skip = False
        self.setup()



    def __call__(self):
        self.counter+=1
        if self.prct_update > 0 and self.counter % self.prct_update == 0:
            percent_tag = "{000:.2f}%".format((self.counter / self.max_c) * 100)
            sys.stdout.write("%s]" % (" " * (self.length - self.progress)))
            sys.stdout.write(percent_tag)
            sys.stdout.flush()

            if self.counter != self.max_c:
                sys.stdout.write("\b" * (self.length + 1 - self.progress + len(percent_tag)))
            else:
                self.end()

        if self.interval > 0 and self.counter % self.interval == 0:
            sys.stdout.write("#")
            self.progress += 1

        return self.counter >= self.max_c

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