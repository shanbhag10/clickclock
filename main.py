import datetime
from controller import window_helper
import time
from database.database_helper import *
from visualization.visualization_helper import refresh_graphs

if __name__ == "__main__":
    # start with a default window
    current_window = "unknown"
    start_time = datetime.datetime.now()
    i = 0
    timer = 0

    # initiate local db connection
    db_context = DataBaseContext()
    db_context.create_table()

    # run an infinite loop at 1s refresh rate
    while True:
        new_window = str(window_helper.get_current_window()).lower()

        # record the stats for current window
        if new_window != current_window:
            new_start_time = datetime.datetime.now()
            duration = new_start_time - start_time
            window_switch_event = WindowSwitchEvent(None, current_window, new_window,
                                                    start_time, duration.total_seconds())
            db_context.insert_data(window_switch_event)

            current_window = new_window
            start_time = new_start_time

        time.sleep(1)
        timer += 1

        if timer >= 10:
            refresh_graphs(db_context)
            timer = 0




