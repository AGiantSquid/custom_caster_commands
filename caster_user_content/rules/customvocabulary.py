from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Text
from dragonfly import MappingRule


class CustomVocabulary(MappingRule):
    pronunciation = "custom vocabulary"
    mapping = {
        "doctor":
            Text("docker "),
        "Lower Schultz":
            Text("shultz"),
        "Ashley Gmail":
            Text("ashley.e.shultz@gmail.com"),
        "e-mail":
            Text(" email "),
        "topple":
            Text("tuple")
    }
    extras = []
    defaults = {}


def get_rule():
    return CustomVocabulary, RuleDetails(name="custom vocabulary")