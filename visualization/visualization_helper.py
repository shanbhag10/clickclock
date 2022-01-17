import matplotlib.pyplot as plt
import itertools


def get_histogram(db_context):
    app_times = db_context.get_app_times()

    top_5_apps = dict(itertools.islice(app_times.items(), 5))

    plt.bar(list(top_5_apps.keys()), top_5_apps.values(), color='cyan', linewidth='5')
    plt.savefig('visualization/histogram.png')


# TODO - Add more graphs

def refresh_graphs(db_context):
    get_histogram(db_context)
