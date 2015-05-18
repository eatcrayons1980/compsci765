from __future__ import with_statement

from pyke import knowledge_engine
from pyke import krb_traceback
import sys
import datetime

engine = knowledge_engine.engine(__file__)


def test():
    engine.reset()

    engine.activate('travelrules')
    #engine.trace('travelrules', 'new_user')

    #f = open('travelfacts.kfb', 'w')
    #s = sys.stdout

    #sys.stdout = f
    #engine.get_kb('travelfacts').dump_universal_facts()
    #engine.get_kb('travelfacts').dump_specific_facts()
    #sys.stdout = s

    try:
        res, plan = engine.prove_1_goal('travelrules.new_user($user)')
    except knowledge_engine.CanNotProve:
        try:
            res, plan = engine.prove_1_goal('travelrules.existing_user($user)')
        except knowledge_engine.CanNotProve:
            sys.exit(-1)
        else:
            print("Welcome back!")
    else:
        print("Welcome to the travel buddy!")
        

    
