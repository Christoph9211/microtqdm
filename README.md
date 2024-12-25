# MicroTqdm

A minimalistic tqdm-like progress bar for MicroPython.

## Description

MicroTqdm is a lightweight progress bar for MicroPython, designed to provide a simple and efficient way to display progress for iterable tasks. It is inspired by the popular `tqdm` library but tailored for the constraints of MicroPython environments.

## Installation

Simply copy the `microtqdm.py` file into your project directory.

## Usage

Here's an example of how to use MicroTqdm:

```python
import time
from microtqdm import MicroTqdm

for _ in MicroTqdm(range(100), desc='Processing', length=30, interval=5):
    time.sleep(0.1)  # Simulate a task taking time
```

## Parameters

- `iterable`: The iterable to iterate over.
- `total` (optional): The total number of elements in the iterable. If not provided, defaults to the length of the iterable.
- `desc` (optional): A description to show in the progress bar. Defaults to an empty string.
- `length` (optional): The length of the progress bar. Defaults to 20.
- `interval` (optional): The interval at which to print an update to the progress bar. Defaults to 10.

## License

This project is licensed under the MIT License.