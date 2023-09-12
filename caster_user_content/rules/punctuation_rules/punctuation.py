from dragonfly import Choice, Repeat, ShortIntegerRef

from castervoice.lib.actions import Key, Text

try:  # Try  first loading  from caster user directory
    from punctuation_support import double_text_punc_dict, text_punc_dict
except ImportError:
    from castervoice.rules.core.punctuation_rules.punctuation_support import double_text_punc_dict, text_punc_dict

from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R


class Punctuation(MergeRule):
    pronunciation = "punctuation"

    mapping = {
        "[<long>] <text_punc> [<npunc>]":
            R(Text("%(long)s" + "%(text_punc)s" + "%(long)s"))*Repeat(extra="npunc"),
        # For some reason, this one doesn't work through the other function
        "[<long>] backslash [<npunc>]":
            R(Text("%(long)s" + "\\" + "%(long)s"))*Repeat(extra="npunc"),
        "<double_text_punc> [<npunc>]":
            R(Text("%(double_text_punc)s") + Key("left"))*Repeat(extra="npunc"),
        "tarp [<npunc>]":
            R(Key("tab"))*Repeat(extra="npunc"),
        "tarsh [<npunc>]":
            R(Key("s-tab"))*Repeat(extra="npunc"),
        'shaber [<npunc>]':
            R(Key("c-rbracket"))*Repeat(extra="npunc"),
        'shable [<npunc>]':
            R(Key("c-lbracket"))*Repeat(extra="npunc"),
    }

    extras = [
        ShortIntegerRef("npunc", 0, 10),
        ShortIntegerRef("npunc100", 0, 100),
        Choice(
            "long", {
                "long": " ",
            }),
        Choice(
            "text_punc", text_punc_dict()),
        Choice(
            "double_text_punc", double_text_punc_dict())
    ]
    defaults = {
        "npunc": 1,
        "npunc100": 1,
        "long": "",
    }


def get_rule():
    return Punctuation, RuleDetails(ccrtype=CCRType.GLOBAL)
