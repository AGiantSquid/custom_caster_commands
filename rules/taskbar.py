
from dragonfly import Key, MappingRule

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
class TaskBar(MappingRule):
    
    mapping = {
        "Dora": Key("w-1"),
        "outlook": Key("w-2"),
        "chromie": Key("w-3"),
        "slacker": Key("w-4"),
        "teamer": Key("w-5"),
        "viz. code": Key("w-6"),
        "termie": Key("w-7"),
    }
    


def get_rule():
    return TaskBar, RuleDetails(name="task bar")
