# MicroTqdm
# 2024-12-24
# Christopher Gibbons
#
# A minimalistic tqdm-like progress bar for MicroPython.
#
import time


class MicroTqdm:
    def __init__(self, iterable, total=None, desc='', length=20, interval=10):
        """
        Initializes a MicroTqdm object to iterate over an iterable.

        Parameters
        ----------
        iterable : iterable
            The iterable to iterate over.
        total : int, optional
            The total number of elements in the iterable. If not provided, defaults to the length of the iterable.
        desc : str, optional
            A description to show in the progress bar. Defaults to an empty string.
        length : int, optional
            The length of the progress bar. Defaults to 20.
        interval : int, optional
            The interval at which to print an update to the progress bar. Defaults to 10.

        Attributes
        ----------
        iterable : iterable
            The iterable to iterate over.
        total : int
            The total number of elements in the iterable.
        desc : str
            A description to show in the progress bar.
        length : int
            The length of the progress bar.
        interval : int
            The interval at which to print an update to the progress bar.
        start_time : float
            The time when the iteration started.
        n : int
            The current number of elements in the iterable.
        last_print_n : int
            The number of elements that were last printed in the progress bar.
        """
        self.iterable = iterable
        self.total = total if total else len(iterable)
        self.desc = desc
        self.length = length
        self.interval = interval
        self.start_time = time.time()
        self.n = 0
        self.last_print_n = 0
             
    # display the completion bar
    def display(self):
        """
        Displays the progress bar with the current completion percentage, 
        the filled portion of the bar, and the elapsed time since the start. 
        This method is called at intervals during iteration to update the 
        progress bar in-place.
        """

        percentage = (self.n / self.total) * 100
        filled_length = int(self.length * self.n // self.total)
        bar = '=' * filled_length + '-' * (self.length - filled_length)
        elapsed_time = time.time() - self.start_time
        print(f'\r{self.desc} |{bar}| {percentage:.2f}% | {self.n}/{self.total} | {elapsed_time:.2f}s', end='\r')

    def __iter__(self):
        """
        Yields each item in the given iterable, displaying a progress bar
        every ``self.interval`` items. When the iterable is exhausted, a
        newline is printed.
        """
        for item in self.iterable:
            yield item
            self.n += 1
            if self.n - self.last_print_n >= self.interval:
                self.display()
                self.last_print_n = self.n
        self.display()
        print()  # Newline at the end of the progress bar

# Usage example:

for _ in MicroTqdm(range(100), desc='Processing', length=30, interval=5):
        time.sleep(0.1)  # Simulate a task taking time

