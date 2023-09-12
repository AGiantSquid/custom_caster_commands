from castervoice.lib import navigation, textformat
from castervoice.lib.actions import Key
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R

from dragonfly import (Dictation, Function, Playback, Repeat, ShortIntegerRef, Text)



def format_text_wrapper(cap, space, textnv):
    '''
    allows defaults for Capitalization and spacing
    that override the default capitalization and spacing
    in nav.py
    '''

    textformat.master_format_text(cap, space, textnv)


def wheel_scroll_up(nnavi500):
    navigation.wheel_scroll('up', nnavi500)


def wheel_scroll_down(nnavi500):
    navigation.wheel_scroll('down', nnavi500)


def _first_letters(textnv):
    Text(''.join([_[0] for _ in textnv.split()])).execute()


def _first_three(textnv):
    Text(textnv[:3]).execute()


def _first_four(textnv):
    Text(textnv[:4]).execute()


class CustomStuff(MergeRule):
    pronunciation = "custom stuff"
    mapping = {
        "open new file":
            R(Key("c-n"), rdescript="Custom Navigation: Open New File"),
        "toggle tab":
            R(Key("c-tab"), rdescript="Next Tab"),
        "Ali | Ollie | Holly":
            R(Key("c-a"), rdescript="Select All"),
        "back tab [<n>]":
            R(Key("s-tab"), rdescript="Previous Tab")*Repeat(extra="n"),
        "(windy | Wendy) lease [<n>]":
            R(Key("w-left"), rdescript="Window Left")*Repeat(extra="n"),
        "(windy | Wendy) ross [<n>]":
            R(Key("w-right"), rdescript="Window Right")*Repeat(extra="n"),
        "mahni lease [<n>]":
            R(Key("sw-left"), rdescript="Monitor Left")*Repeat(extra="n"),
        "manhi ross [<n>]":
            R(Key("sw-right"), rdescript="Monitor Right")*Repeat(extra="n"),
        "workace lease":
            R(Key("cw-left"), rdescript="Workspace Left"),
        "workace ross":
            R(Key("cw-right"), rdescript="Workspace Right"),
        "peach":
            R(Key("c-t"), rdescript="Open New Tabs"),
        "totch":
            R(Key("c-w/20"), rdescript="Close Tab"),
        "Lexi":
            R(Key("s-home"), rdescript="Custom Navigation: Home Key"),
        "Ricksy":
            R(Key("s-end"), rdescript="Custom Navigation: End Key"),
        "snipple":
            R(Key("s-home") + Key("del/5"), rspec="snipple", rdescript="Delete to beginning of line"),
        "(sniper | snipper)":
            R(Key("s-end") + Key("del/5"), rspec="snipper", rdescript="Delete to end of line"),
        "shreep [<nnavi50>]":
            R(Key("s-up"), rspec="shreeep", rdescript="Select a line up")*
            Repeat(extra="nnavi50"),
        "shroom [<nnavi50>]":
            R(Key("s-down"), rspec="shroom", rdescript="Select a line down")*
            Repeat(extra="nnavi50"),
        "(Kate | Kite) [<nnavi50>]":
            R(Key("c-del"), rspec="clear", rdescript="Backspace")*Repeat(extra="nnavi50"),
        "trough [<nnavi50>]":
            R(Key("c-backspace"), rspec="clear", rdescript="Backspace")*
            Repeat(extra="nnavi50"),
        "(chiff | Jeff) [<nnavi3>]":
            R(Function(navigation.left_click))*Repeat(extra="nnavi3"),
        'duke':
            R(Function(navigation.left_click)*Repeat(2)),
        "snitch <textnv>":
            R(Function(_first_letters), rdescript="First letter"),
        "thrack <textnv>":
            R(Function(_first_three), rdescript="First three letters"),
        "quatro <textnv>":
            R(Function(_first_four), rdescript="First four letters"),
        "cram <textnv>":
            R(Function(format_text_wrapper, cap=3, space=1), rdescript="camelCase"),
        "smash <textnv>":
            R(Function(format_text_wrapper, cap=5, space=1),
              rdescript="lowercasenospaces"),
        "squash <textnv>":
            R(Function(format_text_wrapper, cap=5, space=0),
              rdescript="lowercase with spaces"),
        "scrodge [<nnavi50>]":
            R(Function(wheel_scroll_down), rdescript="Wheel Scroll")*Repeat(extra="nnavi50"),
        "scroop [<nnavi50>]":
            R(Function(wheel_scroll_up), rdescript="Wheel Scroll")*Repeat(extra="nnavi50"),
        'snore':
            R(Playback([(["go", "to", "sleep"], 0.0)])),

        # The following commands of been enabled via words.txt
        # If Caster gets rid of transformers, reenable these words
        # "marco":
        #     R(Key("c-f"), rdescript="Find"),
        # "dizzle [<n>]":
        #     R(Key("c-z"), rdescript="Undo")*Repeat(extra="n"),
        # "rizzle [<n>]":
        #     R(Key("c-y"), rdescript="Redo")*Repeat(extra="n"),
        # "(windy | Wendy) Max":
        #     R(Key("w-up"), rdescript="Maximize Window"),
        # "snatch":
        #     R(Key("c-x"), rdescript="Open New Tab"),
        # "junk [<nnavi50>]":
        #     R(Key("backspace/5:%(nnavi50)d"), rspec="clear", rdescript="Backspace"),
        # "spunk [<nnavi50>]":
        #     R(Key("del/5"), rspec="deli", rdescript="Delete")*Repeat(extra="nnavi50"),
        # "fish [<nnavi50>]":
        #     R(Key("c-right"), rspec="fish", rdescript="Jump word to the right")*
        #     Repeat(extra="nnavi50"),
        # "fame [<nnavi50>]":
        #     R(Key("c-left"), rspec="fame", rdescript="Jump word to the Left")*
        #     Repeat(extra="nnavi50"),
        # "scrish [<nnavi50>]":
        #     R(Key("cs-right"), rspec="scrish", rdescript="Select word to the right")*
        #     Repeat(extra="nnavi50"),
        # "scram [<nnavi50>]":
        #     R(Key("cs-left"), rspec="scram", rdescript="Select a word to the left")*
        #     Repeat(extra="nnavi50"),

    }
    extras = [
        ShortIntegerRef("nnavi3", 1, 4),
        ShortIntegerRef("n", 1, 10),
        ShortIntegerRef("nnavi50", 1, 50),
        Dictation("textnv"),
    ]
    defaults = {"n": 1, "nnavi50": 1, "textnv": ""}


def get_rule():
    details = RuleDetails(ccrtype=CCRType.GLOBAL)
    return CustomStuff, details
