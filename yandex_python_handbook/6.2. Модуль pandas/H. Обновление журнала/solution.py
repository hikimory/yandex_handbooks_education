import pandas as pd


def update(journal):
    new_journal = journal.copy()
    new_journal['average'] = new_journal[['maths', 'physics', 'computer science']].mean(axis=1)
    new_journal = new_journal.sort_values(by=['average', 'name'], ascending=[False, True])
    return new_journal


def update2(journal):
    new_journal = journal.copy()
    new_journal = new_journal.assign(
        average=lambda x: x[['maths', 'physics', 'computer science']].mean(axis=1)
    )
    new_journal = new_journal.sort_values(by=['average', 'name'], ascending=[False, True])
    return new_journal