from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback, 
                       IntegerRef, Dictation, Choice, WaitWindow)
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse
from dragonfly import Text


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
    }
    extras = []
    defaults = {}


def get_rule():
    return CustomVocabulary, RuleDetails(name="custom vocabulary")