def run():
    inputs = ['HackerRank.com presents "Pythonist 2".', 'Pythonist 2']

    for ent in inputs:
        print(split_and_join(ent))


def split_and_join(ent: str):
    return '-'.join(ent.split(" "))
