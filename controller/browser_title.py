from brotab import main as btm
from brotab.api import MultipleMediatorsAPI
from brotab.main import create_clients


def get_browser_title():
    api = MultipleMediatorsAPI(create_clients())
    result = api.list_tabs([])[1:3]
    for line in result:
        print(line)


def get_browser_client():
    clients = btm.create_clients()
    if not clients:
        raise Exception("No clients found!")
    browser_matches = [cl for cl in clients if cl._get_browser() == "firefox"]
    return browser_matches[0]


def parse_tabs(client):
    """
    returns a list of Tab objects
    """
    tabs = client.list_tabs_safe(None)
    for i, tab in enumerate(tabs):
        tabs[i] = tab.split('\t')
    # sanity-check tab lengths after parsing - result should be {3}
    tab_list_lengths = set([len(tab) for tab in tabs])
    try:
        assert ( tab_list_lengths == {3})
    except AssertionError:
        faulty_tab_strs = [repr(tab) for tab in tabs if len(tab) != 3]
        faulty_tabs_str = ", ".join(faulty_tab_strs)
        raise ValueError("Tab info parsing problem! Tab list lengths after parsing: {}, faulty tabs: {}".format(repr(tab_list_lengths), faulty_tabs_str))
    for i, tab in enumerate(tabs):
        tab[1:1] = tab[0].split('.')
        tab.pop(0)
        tabs[i] = Tab(*tabs[i])

    print(tabs)
    return tabs


class Tab():
    def __init__(self, prefix, window, id, name, url):
        self.prefix = prefix
        self.window = window
        self.id = id
        self.name = name
        self.url = url

    def get_full_id(self):
        return ".".join([self.prefix, self.window, self.id])

    def to_string(self):
        return "\t".join([self.get_full_id(), self.name, self.url])