import dragonfly


def double_text_punc_dict():
    return {
        "quotes":                              "\"\"",
        "Quach it":                            "''",
        "tickris":                             "``",
        "prekris":                             "()",
        "brax":                                "[]",
        "curly":                               "{}",
        "angle":                               "<>",
    }


def _inv_dtpb():
    return {v: k for k, v in double_text_punc_dict().items()}


def text_punc_dict():
    # Insurers comma is recognized consistently with DNS/Natlink and
    # if/else statement workaround engines that do not expect punctuation symbol as a command
    if hasattr(dragonfly.get_current_engine(), "name"):
        if (dragonfly.get_current_engine().name == 'natlink'):
            comma = "(comma | ,)"
        else:
            comma = "comma"
    else:
        comma = "comma"

    _id = _inv_dtpb()
    return {
        "skoosh":                                             " ",
        "bang":                                               "!",
        "hash tag | pound sign | pounder":                    "#",
        "Dolly":                                              "$",
        "Percy":                                              "%",
        "ampersand":                                          "&",
        "Quach it | chicky":                                  "'",
        "prekorp":                                            "(",
        "prekos":                                             ")",
        "starling":                                           "*",
        "plus":                                               "+",
        comma:                                                ",",
        "minus":                                              "-",
        "period | dot":                                       ".",
        "slash":                                              "/",
        "deckle":                                             ":",
        "sinker":                                             ";",
        "[is] less than | langle ":                           "<",
        "[is] less [than] [or] equal [to]":                  "<=",
        "equals":                                             "=",
        "[is] equal to":                                   " == ",
        "[is] greater than | wrangle ":                       ">",
        "[is] greater [than] [or] equal [to]":               ">=",
        "questo":                                             "?",
        "(atty | at symbol)":                                 "@",
        "brackorp ":                                          "[",
        "shawls | backslash":                                "\\",
        "brackos":                                            "]",
        "carrot":                                             "^",
        "crunder":                                            "_",
        "tinker":                                             "`",
        "kirksorp":                                           "{",
        "kirkos":                                             "}",
        "pipe (sim | symbol)":                                "|",
        "tilde":                                              "~",

        "Schrock it | shrocket":                           " => ",
        "tharrow":                                         " -> ",

    }
