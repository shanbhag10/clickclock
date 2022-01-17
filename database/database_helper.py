import sqlite3 as sl

database = 'database/clickclock.db'
table_name = 'click_clock_test'


class DataBaseContext:
    def __init__(self):
        self.connection = sl.connect(database)
        self.cursor = self.connection.cursor()
        print("Connected to database successfully")

    def create_table(self):
        create_table_sql = 'create table if not exists ' + table_name + \
                           ' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ' + \
                           ' timestamp TEXT, window TEXT, next_window TEXT, duration REAL)'
        self.cursor.execute(create_table_sql)
        self.connection.commit()

    def insert_data(self, window_switch_event):
        ignore_apps = ['loginwindow', 'unknown']
        if window_switch_event.window in ignore_apps :
            return

        print(window_switch_event.__dict__)
        insert_data_sql = 'insert into ' + table_name + \
                          ' (id, timestamp, window, next_window, duration) values (NULL, ?, ?, ?, ?)'
        self.cursor.execute(insert_data_sql, (window_switch_event.timestamp, window_switch_event.window,
                                              window_switch_event.next_window, window_switch_event.duration))
        self.connection.commit()

    def get_all_events(self):
        cursor = self.connection.execute("SELECT * from " + table_name)
        all_events = []
        for row in cursor:
            all_events.append(event_from_list(row))

        return all_events

    def get_app_times(self):
        cursor = self.connection.execute("SELECT window, SUM(duration) as total_duration from " + table_name +
                                         " group by window order by total_duration desc")
        app_times = {}
        for row in cursor:
            app_times[row[0]] = row[1]

        return app_times


class WindowSwitchEvent:
    def __init__(self, id, window, next_window, timestamp, duration):
        self.id = id
        self.window = window
        self.next_window = next_window
        self.timestamp = timestamp
        self.duration = duration


def event_from_list(row):
    return WindowSwitchEvent(row[0], row[1], row[2], row[3], row[4])
