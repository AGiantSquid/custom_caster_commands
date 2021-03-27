
from castervoice.lib.const import CCRType
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse

from dragonfly import ShortIntegerRef
from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback, 
                       IntegerRef, Dictation, Choice, WaitWindow)


class CustomPunctuation(MergeRule):

    mapping = {

        # my custom overrides
        "double quotes": Key("dquote"),
        "Quach it": Key("apostrophe"),
        "equals | equal to": Text("="),
        "equeft": Text(" = "),
        "Schrock it | shrocket": Text(" => "),
        "not equals | not equal to": Text(" != "),
        "is equal to": Text(" == "),
        "[is] greater than": Text(" > "),
        "[is] less than": Text(" < "),
        "[is] greater [than] [or] equal [to]": Text(" >= "),
        "[is] less [than] [or] equal [to]": Text(" <= "),
        "deplush": Text(" + "),
        "plus": Text("+"),
        "pluqual | Luke while": Text(" += "),
        "deminus": Text(" - "),
        "minus": Text("-"),
        "minqual | min call": Text(" -= "),
        "min twice | mintwice": Text("--"),

        # this is same as the default punctuation
        "sinker": Key("semicolon"),
        "prekris": Key("lparen"),
        "prekorp": Key("lparen"),
        "prekos": Key("rparen"),
        "brax": Key("lbracket"),
        "brackorp": Key("lbracket"),
        "brackos": Key("rbracket"),
        "curly": Key("lbrace"),
        "kirksorp": Key("lbrace"),
        "kirkos": Key("rbrace"),
        "angle": Key("langle"),
        "wrangle": Key("rangle"),
        "(pipe | pipes) (sim | symbol)": Text("|"),
        "pipes and": Text("|"),
        'skoosh [<npunc>]': Key("space"),
        "clamor": Text("!"),
        "deckle": Text(":"),
        "starling": Key("asterisk"),
        "questo": Text("?"),
        "comma": Text(","),
        "carrot": Text("^"),
        "(period | dot)": Text("."),
        "at sign": Text("@"),
        "hash tag | pound sign | pounder": Text("#"),
        "apostrophe": Text("'"),
        "tinker": Text("`"),
        "crunder": Text("_"),
        "shawls": Text("\\"),
        "slash": Text("/"),
        "Dolly": Text("$"),
        "Percy": Key("percent"),
        'tarp [<npunc>]': Key("tab"),
        'tarsh [<npunc>]': Key("s-tab"),
        'shaber [<npunc>]': Key("c-rbracket"),
        'shable [<npunc>]': Key("c-lbracket"),
        "swipe": Text(", "),
    }
    pronuniation= "custom punctuation"
    extras = [
        ShortIntegerRef("npunc", 0, 10),
    ]
    defaults = {
        "npunc": 1,
    }


def get_rule():
    details = RuleDetails(ccrtype=CCRType.GLOBAL)
    return CustomPunctuation, details
