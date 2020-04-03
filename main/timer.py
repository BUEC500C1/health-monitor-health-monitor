import threading

#repeats function every X seconds
def timer(seconds,function):
    t = threading.Event()
    while not t.wait(seconds):
        function()