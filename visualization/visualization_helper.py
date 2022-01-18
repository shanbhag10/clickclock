import matplotlib.pyplot as plt


def get_histogram(db_context):
    app_times = db_context.get_app_times(5)
    keys = list(app_times.keys())
    for i in range(len(keys)):
        keys[i] = keys[i].replace(" ", "\n")

    print(app_times)
    plt.bar(range(len(keys)), app_times.values(), color='#009be9')

    plt.title("Top 5 Apps")
    plt.ylabel("Active Time in seconds")
    plt.xticks(range(len(keys)), keys)

    plt.savefig('visualization/histogram.png')


# TODO - Add more graphs

def refresh_graphs(db_context):
    get_histogram(db_context)
