from __future__ import with_statement

from pyke import knowledge_engine
from pyke import krb_traceback
import sys
import datetime

def run():
    init_shortterm_memory()
    init_user()

def init_shortterm_memory():
    shortterm = open('shortterm.kfb', 'w')
    shortterm.write("# Activated " + str(datetime.datetime.now()) + "\n")
    shortterm.close()

def init_user():
    engine = knowledge_engine.engine(__file__)
    engine.reset()
    engine.activate('travelrules')

    try:
        result, plan = engine.prove_1_goal('travelrules.new_user($user)')
    except knowledge_engine.CanNotProve:
        try:
            result, plan = engine.prove_1_goal('travelrules.existing_user($user)')
        except knowledge_engine.CanNotProve:
            print("Could not establish user model. Exiting with -1.")
            sys.exit(-1)

    write_shortterm_longterm(engine)

def write_shortterm(engine):
    shortterm = open('shortterm.kfb', 'a')
    temp = sys.stdout
    sys.stdout = shortterm
    engine.get_kb('shortterm').dump_universal_facts()
    engine.get_kb('shortterm').dump_specific_facts()
    sys.stdout = temp
    shortterm.close()

def write_longterm(engine):
    longterm = open('travelfacts.kfb', 'a')
    temp = sys.stdout
    sys.stdout = longterm
    print("\n\n# Added " + str(datetime.datetime.now()))
    engine.get_kb('travelfacts').dump_specific_facts()
    sys.stdout = temp
    longterm.close()

def write_shortterm_longterm(engine):
    write_shortterm(engine)
    write_longterm(engine)
    
