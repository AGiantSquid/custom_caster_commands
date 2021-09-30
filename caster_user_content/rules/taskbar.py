
from dragonfly import Key, MappingRule

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
class TaskBar(MappingRule):

    mapping = {
        "Dora": Key("w-1"),
        "outlook": Key("w-2"),
        "chromie": Key("w-3"),
        "teamer": Key("w-4"),
        "viz. code": Key("w-5"),
        "termie": Key("w-6"),
    }



def get_rule():
    return TaskBar, RuleDetails(name="task bar")
