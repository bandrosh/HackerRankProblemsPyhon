def run():
    inputs = ['HackerRank.com presents "Pythonist 2".', 'Pythonist 2']

    for ent in inputs:
        print(swap_case(ent))


def swap_case(s: str):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in list(s)])
