from pen_plotter import PenPlotter
import time

app = PenPlotter()

while True:
    app.run()

    print("Waiting to run again...")
    time.sleep(2)
