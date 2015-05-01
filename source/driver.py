from __future__ import with_statement

from pyke import knowledge_engine
import sys

engine = knowledge_engine.engine(__file__)

def test():
    engine.reset()

    engine.activate('travelrules')

    engine.print_stats()

    with engine.prove_goal(
            'travelrules.similar_to($loc1, $loc2)') as gen:
        for vars, plan in gen:
            print(loc1 + ' is similar to ' + loc2)
