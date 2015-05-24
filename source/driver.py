from __future__ import with_statement

from pyke import knowledge_engine
from pyke import krb_traceback
import sys
import datetime
import random

def run():
    random.seed()
    wipe_shortterm_memory()
    e = launch_engine()
    frustration = 0
    while frustration < 100:
        
        # suggest place with same activities as other places the user has been
        x = random.randint(0,100)
        try:
            res,plan = e.prove_1_goal(
                    'travelrules.recommender_same_activities($place,' + str(x) + ')'
                    )
        except knowledge_engine.CanNotProve:
            pass
        else:
            break

        # suggest place with activities the user likes
        x = random.randint(0,100)
        try:
            res,plan = e.prove_1_goal(
                    'travelrules.recommender_likes_activities($place,' + str(x) + ')'
                    )
        except knowledge_engine.CanNotProve:
            pass
        else:
            break

        frustration = frustration + 5

    write_longterm(e)

def wipe_shortterm_memory():
    shortterm = open('shortterm.kfb', 'w')
    shortterm.write("# Shortterm memory wiped: " + str(datetime.datetime.now()) + "\n")
    shortterm.close()

def launch_engine():
    engine = knowledge_engine.engine(__file__)
    engine.reset()
    engine.activate('travelrules')
    return engine

def write_shortterm(engine):
    shortterm = open('shortterm.kfb', 'a')
    temp = sys.stdout
    sys.stdout = shortterm
    print("\n\n# Added " + str(datetime.datetime.now()))
    engine.get_kb('shortterm').dump_specific_facts()
    sys.stdout = temp
    shortterm.close()

def write_longterm(engine):
    longterm = open('longterm.kfb', 'a')
    temp = sys.stdout
    sys.stdout = longterm
    print("\n\n# Added " + str(datetime.datetime.now()))
    engine.get_kb('longterm').dump_specific_facts()
    sys.stdout = temp
    longterm.close()

def write_shortterm_longterm(engine):
    write_shortterm(engine)
    write_longterm(engine)
    
