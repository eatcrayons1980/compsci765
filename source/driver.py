from __future__ import with_statement

from pyke import knowledge_engine
import sys

engine = knowledge_engine.engine(__file__)

def test():
    engine.reset()

    engine.activate('travelrules')

    engine.print_stats()

    engine.get_kb('travelfacts').dump_universal_facts()
    engine.get_kb('travelfacts').dump_specific_facts()
